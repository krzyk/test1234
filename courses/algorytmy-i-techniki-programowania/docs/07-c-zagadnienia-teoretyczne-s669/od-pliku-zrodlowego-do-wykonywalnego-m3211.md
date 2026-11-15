# Od pliku źródłowego do wykonywalnego

Kod źródłowy w języku C++ (plik .cpp) jest niezrozumiały dla procesora. Dzieje się tak dlatego, że C++ jest językiem wysokiego poziomu i aby procesor mógł go wykonać, musi go odpowiednio "przetłumaczyć" na swój język, czyli ciąg 0 i 1 (kod maszynowy). Tym tłumaczeniem zajmuje się specjalne oprogramowanie, jakim jest <u>**kompilator.**</u>

Kompilacja to proces wytwarzania pliku wykonywalnego (czyli kodu maszynowego). Plik wykonywalny (w Windows to .exe od ang. executable) zawiera kod programu w języku maszynowym charakterystycznym **<u>tylko dla danego systemu operacyjnego i procesora. </u>**Dlatego też nie jest przenośny między platformami, tzn. nie możemy pliku wykonywalnego otrzymanego np. na Mac przenieść na Win lub w obrębie tego samego systemu przenieść na komputer z innym procesorem. **Kod maszynowy NIE JEST PRZENOŚNY.**  Natomiast sam kod źródłowy jest niezależny od platformy.

Kompilacja to proces wieloetapowy, w którym kod źródłowy przechodzi przez kilka faz przed uzyskaniem gotowego pliku wykonywalnego.

**Etapy kompilacji:**

<ol>
<li><u><strong><strong data-end="15" data-start="0">Preprocesor</strong> </strong></u>w C++ to narzędzie, które działa przed kompilacją właściwego kodu. Jego zadaniem jest przygotowanie kodu źródłowego poprzez wykonanie tzw. dyrektyw preprocesora (poleceń rozpoczynających się od <code data-end="231" data-start="228">#</code> )<ol>
<li>
<ul data-end="1013" data-start="402">
<li data-end="578" data-start="402">
<p data-end="578" data-start="404"><strong data-end="416" data-start="404">Zadanie:</strong> Na tym etapie kompilator przetwarza dyrektywy preprocesora (np. <code data-end="491" data-start="481">#include</code>, <code data-end="502" data-start="493">#define</code>, <code data-end="512" data-start="504">#ifdef</code>), które są używane do modyfikacji kodu przed właściwą kompilacją.</p>
</li>
<li data-end="883" data-start="582">
<p data-end="599" data-start="584"><strong data-end="598" data-start="584">Działania:</strong></p>
<ul data-end="883" data-start="605">
<li data-end="695" data-start="605">
<p data-end="695" data-start="607"><strong data-end="641" data-start="607">Wstawianie plików nagłówkowych</strong> – np. <code data-end="669" data-start="648">#include &lt;iostream&gt;</code> wstawia kod z biblioteki.</p>
</li>
<li data-end="779" data-start="701">
<p data-end="779" data-start="703"><strong data-end="727" data-start="703">Definiowanie stałych</strong> – np. <code data-end="751" data-start="734">#define PI 3.14</code> tworzy zamienniki tekstowe.</p>
</li>
<li data-end="883" data-start="785">
<p data-end="883" data-start="787"><strong data-end="811" data-start="787">Warunkowa kompilacja</strong> – kod może być włączany lub wyłączany na podstawie zdefiniowanych makr - np. #ifdef DEBUG std::cout &lt;&lt; "Debug mode\n"; #endif</p>
</li>
</ul>
</li>
<li data-end="1013" data-start="887">
<p data-end="1013" data-start="889"><strong data-end="899" data-start="889">Wynik:</strong> Powstaje plik źródłowy, w którym te dyrektywy są już rozwiązywane, a kod jest przygotowany do dalszej kompilacji.</p>
</li>
</ul>
</li>
</ol></li>
<li><u><strong>Kompilacja</strong></u></li>
<li>
<a id="yui_3_13_0_2_1746690889450_790"></a><ul data-end="1892" data-start="1274">
<li data-end="1438" data-start="1274">
<p data-end="1438" data-start="1276"><strong data-end="1288" data-start="1276">Zadanie:</strong> Kompilator tłumaczy kod źródłowy (po przetworzeniu przez preprocesor) na kod pośredni lub <strong data-end="1400" data-start="1383">kod maszynowy,</strong> ale jeszcze nie łączy go w całość</p>
</li>
<a id="yui_3_13_0_2_1746690889450_789"></a><li data-end="1747" data-start="1442">
<a id="yui_3_13_0_2_1746690889450_788"></a><p data-end="1458" data-start="1444"><strong data-end="1458" data-start="1444">Działania:</strong></p>
<a id="yui_3_13_0_2_1746690889450_795"></a><ul data-end="1747" data-start="1464">
<li data-end="1541" data-start="1464">
<p data-end="1541" data-start="1466">Analizuje składnię programu, upewniając się, że jest zgodna z regułami C++.</p>
</li>
<a id="yui_3_13_0_2_1746690889450_794"></a><li data-end="1602" data-start="1547">
<a id="yui_3_13_0_2_1746690889450_793"></a><p data-end="1602" data-start="1549">Sprawdza typy danych, deklaracje zmiennych i funkcji.</p>
</li>
<li data-end="1747" data-start="1608">
<p data-end="1747" data-start="1610">Tłumaczy instrukcje na kod maszynowy, ale bez pełnego rozwiązania odniesień między różnymi plikami (np. wywołań funkcji z innych plików).</p>
</li>
</ul>
</li>
<li data-end="1892" data-start="1751">
<p data-end="1892" data-start="1753"><strong data-end="1763" data-start="1753">Wynik:</strong> Powstaje plik <strong data-end="1791" data-start="1778">obiektowy</strong> (<code data-end="1797" data-start="1793">.o</code> lub <code data-end="1808" data-start="1802">.obj</code>), który zawiera kod maszynowy, ale jeszcze nie jest w pełni gotowy do uruchomienia.</p>
<p></p>
</li>
</ul>
</li>
<li data-end="1892" data-start="1751">
<a id="yui_3_13_0_2_1746690889450_815"></a><p data-end="2026" data-start="2000"><u><strong data-end="2026" data-start="2000">Łączenie (Linkowanie):</strong></u></p>
<a id="yui_3_13_0_2_1746690889450_829"></a><ul data-end="2759" data-start="2030">
<li data-end="2234" data-start="2030">
<p data-end="2234" data-start="2032"><strong data-end="2044" data-start="2032">Zadanie:</strong> Łączenie to proces, w którym <strong data-end="2084" data-start="2074">linker (konsolidator)</strong> łączy pliki obiektowe (<code data-end="2112" data-start="2108">.o</code>, <code data-end="2120" data-start="2114">.obj</code>) w jeden plik wykonywalny, rozwiązując odniesienia między nimi (np. do funkcji zadeklarowanych w innych plikach).</p>
</li>
<a id="yui_3_13_0_2_1746690889450_828"></a><li data-end="2666" data-start="2238">
<a id="yui_3_13_0_2_1746690889450_827"></a><p data-end="2254" data-start="2240"><a id="yui_3_13_0_2_1746690889450_826"></a><strong data-end="2254" data-start="2240">Działania:</strong></p>
<ul data-end="2666" data-start="2260">
<li data-end="2387" data-start="2260">
<p data-end="2387" data-start="2262"><strong data-end="2293" data-start="2262">Łączenie plików obiektowych</strong> – jeśli program składa się z wielu plików <code data-end="2342" data-start="2336">.cpp</code>, linker połączy je w jeden plik wykonywalny.</p>
</li>
<li data-end="2508" data-start="2393">
<p data-end="2508" data-start="2395"><strong data-end="2419" data-start="2395">Dołączanie bibliotek</strong> – np. standardowa biblioteka C++</p>
</li>
<li data-end="2666" data-start="2514">
<p data-end="2666" data-start="2516"><strong data-end="2543" data-start="2516">Rozwiązywanie odniesień</strong> – jeśli funkcja jest zadeklarowana w jednym pliku, a wywołana w innym, linker zajmuje się rozwiązywaniem takich odniesień  (łączy definicje funkcji i zmiennych rozrzuconych po różnych plikach)</p>
</li>
</ul>
</li>
</ul>
</li>
<li data-end="3145" data-start="2980">
<p data-end="3008" data-start="2983" style="text-align: left;"><u><strong data-end="3008" data-start="2983">Wykonywanie programu:</strong></u></p>
</li>
<li data-end="1892" data-start="1751"><ol data-end="3145" data-start="2980" start="4">
<li style="list-style-type: none;">
<ul data-end="3145" data-start="3012">
<li data-end="3145" data-start="3012">
<p data-end="3145" data-start="3014">Po zakończeniu procesu kompilacji i linkowania, powstaje <strong data-end="3091" data-start="3071">plik wykonywalny</strong>, który można uruchomić na danym systemie operacyjnym.</p>
</li>
</ul>
</li>
</ol></li>
</ol>
