"""Regression tests for privacy boundaries, conversion and safe repeat imports."""
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
import zipfile

from import_moodle import Archive, Importer, write_output


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.members = {
            'moodle_backup.xml': '<moodle_backup><information><original_wwwroot>https://old.example</original_wwwroot></information></moodle_backup>',
            'course/course.xml': '<course id="37" contextid="50"><fullname>Żółć i C++</fullname><visible>1</visible></course>',
            'sections/section_1/section.xml': '<section id="1"><number>0</number><name>Rozdział</name><visible>1</visible><sequence>1,2,3,4,5,6,7</sequence></section>',
            'files.xml': '<files/>',
            # These private backup records must never be copied into output.
            'users.xml': '<users><user><email>PRIVATE_USER</email></user></users>',
        }
        self.add_activity('1', 'page', '<name>Przykład</name><content>&lt;p&gt;#include&amp;lt;cmath&amp;gt;&lt;/p&gt;&lt;p&gt;&lt;a href="$@PAGEVIEWBYID*2@$"&gt;drugi&lt;/a&gt;&lt;/p&gt;&lt;p&gt;&lt;span style="font-family:monospace"&gt;int n=0;&lt;/span&gt;&lt;/p&gt;')
        self.add_activity('2', 'page', '<name>Przykład</name><content>&lt;p&gt;Zażółć gęślą jaźń&lt;/p&gt;</content>')
        # Fix content closure in first test lesson.
        self.members['activities/page_1/page.xml'] = self.members['activities/page_1/page.xml'].replace('</page>', '</content></page>')
        self.add_activity('3', 'page', '<name>Ukryty</name><content>PRIVATE_HIDDEN</content>', '<visible>0</visible>')
        self.add_activity('4', 'book', '<name>Książka</name><chapters><chapter id="11"><title>Pierwszy</title><pagenum>1</pagenum><subchapter>0</subchapter><hidden>0</hidden><content>&lt;p&gt;Treść&lt;/p&gt;</content></chapter><chapter id="12"><title>Drugi</title><pagenum>2</pagenum><subchapter>1</subchapter><hidden>0</hidden><content>&lt;p&gt;Podrozdział&lt;/p&gt;</content></chapter><chapter id="13"><title>Tajny</title><pagenum>3</pagenum><hidden>1</hidden><content>PRIVATE_CHAPTER</content></chapter></chapters>')
        self.add_activity('5', 'quiz', '<name>Quiz</name><attempts>PRIVATE_ATTEMPT</attempts>')
        self.add_activity('6', 'label', '<name>Etykieta</name><intro>&lt;hr/&gt;</intro>')
        self.add_activity('7', 'page', '<name>Ograniczony</name><content>PRIVATE_RESTRICTED</content>', '<visible>1</visible><availability>{"op":"&amp;","c":[{"type":"group"}]}</availability>')

    def tearDown(self):
        self.temp.cleanup()

    def add_activity(self, mid, kind, content, visibility='<visible>1</visible>'):
        prefix = f'activities/{kind}_{mid}/'
        self.members[prefix + 'module.xml'] = f'<module id="{mid}"><modulename>{kind}</modulename>{visibility}</module>'
        self.members[prefix + kind + '.xml'] = f'<activity id="{mid}" moduleid="{mid}" contextid="{mid}0"><{kind}>{content}</{kind}></activity>'

    def archive(self, tar=False):
        path = self.root / ('input.tar.gz' if tar else 'input.mbz')
        if tar:
            with tarfile.open(path, 'w:gz') as handle:
                for name, content in self.members.items():
                    data = content.encode()
                    member = tarfile.TarInfo(name)
                    member.size = len(data)
                    handle.addfile(member, io.BytesIO(data))
        else:
            with zipfile.ZipFile(path, 'w') as handle:
                for name, content in self.members.items():
                    handle.writestr(name, content)
        return path

    def generate(self, tar=False):
        importer = Importer(self.archive(tar), 'https://example.github.io/repo/course/')
        return importer, importer.generate()

    def test_privacy_and_visibility(self):
        importer, output = self.generate()
        published = b'\n'.join(v for k, v in output.items() if k.startswith('docs/'))
        self.assertNotIn(b'PRIVATE_', published)
        self.assertNotIn('3', importer.targets)
        self.assertNotIn('7', importer.targets)
        self.assertEqual(importer.stats['hidden_activities'], 2)  # page + book chapter
        self.assertEqual(importer.stats['unsupported_visible_activities'], 1)

    def test_duplicate_titles_links_and_literal_cpp(self):
        importer, output = self.generate()
        first, second = importer.targets['1'], importer.targets['2']
        self.assertNotEqual(first, second)
        text = output['docs/' + first].decode()
        self.assertIn(Path(second).name, text)
        self.assertIn('&lt;cmath&gt;', text)
        self.assertIn('```cpp\nint n=0;', text)
        self.assertIn('Zażółć gęślą jaźń', output['docs/' + second].decode())

    def test_books_and_label_order(self):
        importer, output = self.generate()
        self.assertEqual(importer.stats['book_chapters'], 2)
        self.assertNotIn('13', importer.chapters)
        self.assertEqual(importer.targets['6'], '00-rozdzial-s1/index.md')
        self.assertIn('---', output['docs/00-rozdzial-s1/index.md'].decode())
        self.assertIn('Pierwszy', output['zensical.toml'].decode())

    def test_repeat_import_and_edit_protection(self):
        _, output = self.generate()
        target = self.root / 'out'
        write_output(target, output)
        before = (target / '.moodle-import.json').read_bytes()
        write_output(target, output)
        self.assertEqual(before, (target / '.moodle-import.json').read_bytes())
        page = next(k for k in output if k.startswith('docs/') and k.endswith('.md'))
        (target / page).write_text('Teacher edit')
        (target / 'unrelated.txt').write_text('Keep me')
        with self.assertRaisesRegex(ValueError, 'edited or unrelated'):
            write_output(target, output)
        self.assertEqual((target / page).read_text(), 'Teacher edit')
        write_output(target, output, overwrite=True)
        self.assertEqual((target / 'unrelated.txt').read_text(), 'Keep me')

    def test_unrelated_file_cannot_be_overwritten_even_with_flag(self):
        target = self.root / 'out'
        target.mkdir()
        (target / 'note.md').write_text('unrelated')
        with self.assertRaises(ValueError):
            write_output(target, {'note.md': b'new'}, overwrite=True)

    def test_tar_backup(self):
        zip_import, zip_output = self.generate()
        tar_import, tar_output = self.generate(tar=True)
        self.assertEqual(zip_import.targets, tar_import.targets)
        self.assertEqual(zip_output['docs/index.md'], tar_output['docs/index.md'])

    def test_unsafe_archive_and_output_paths(self):
        self.members['../escape'] = 'bad'
        with self.assertRaisesRegex(ValueError, 'Unsafe archive'):
            Archive(self.archive())
        with self.assertRaisesRegex(ValueError, 'Unsafe output'):
            write_output(self.root / 'out', {'../escape': b'bad'})

    def test_adjacent_editor_formatting_preserves_rendered_text(self):
        import markdown
        from bs4 import BeautifulSoup
        self.add_activity('2', 'page', '<name>Przykład</name><content>&lt;p&gt;&lt;em&gt;&lt;strong&gt;T&lt;/strong&gt;&lt;strong&gt;samochod&lt;/strong&gt;&lt;/em&gt;. Będziemy&lt;/p&gt;&lt;ol&gt;&lt;li&gt;&lt;em&gt;Inicjalizacja&lt;/em&gt;&lt;i&gt; bezpośrednia&lt;br/&gt;&lt;/i&gt;&lt;code&gt;int x(1);&lt;/code&gt;&lt;/li&gt;&lt;/ol&gt;</content>')
        importer, output = self.generate()
        rendered = markdown.markdown(output['docs/' + importer.targets['2']].decode())
        text = BeautifulSoup(rendered, 'html.parser').get_text()
        self.assertIn('Tsamochod. Będziemy', text)
        self.assertIn('int x(1);', text)
        self.assertNotIn('klzzwxh', text)

    def test_missing_image_reported_without_placeholder_leak(self):
        self.add_activity('2', 'page', '<name>Przykład</name><content>&lt;p&gt;&lt;img src="@@PLUGINFILE@@/missing.png" alt="Schemat"/&gt;&lt;/p&gt;</content>')
        importer, output = self.generate()
        self.assertEqual(len(importer.unresolved), 1)
        page = output['docs/' + importer.targets['2']].decode()
        self.assertIn('Brak obrazu', page)
        self.assertNotIn('@@PLUGINFILE@@', page)


if __name__ == '__main__':
    unittest.main()
