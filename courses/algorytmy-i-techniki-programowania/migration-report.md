# Moodle migration report

Original course: **algorytm i techniki programowania** (ID 37).

Archive: ZIP, Moodle 2.6.5 (Build: 20140908), backup 2.6.

## Statistics

| Metric | Count |
| --- | ---: |
| resources | 46 |
| exported_sections | 20 |
| pages | 94 |
| labels | 16 |
| markdown_files | 161 |
| book_chapters | 0 |
| attachments | 77 |
| hidden_activities | 56 |
| unsupported_visible_activities | 4 |
| withheld_for_review | 1 |
| source_sections | 23 |
| source_activities | 217 |
| unresolved_references | 11 |

Source activity types: assign: 1, forum: 2, label: 16, page: 104, quiz: 17, resource: 77. No Books or Folders occur in this backup.

Extracted file types:

- application/msword: 3
- application/pdf: 31
- application/vnd.openxmlformats-officedocument.wordprocessingml.document: 3
- application/zip: 3
- image/gif: 2
- image/jpeg: 18
- image/png: 11
- text/plain: 6

## Publication and privacy

The backup contains private user records and submission data. Only teaching fields from course/section metadata and allowlisted Page, Book, Label, Resource, Folder and URL modules are read for export. User profiles, enrolments, grades, quiz attempts/questions, forum discussions, submissions, completion data and logs are never copied. File components are allowlisted by exported activity context and content area; submission and question files are excluded. File metadata such as uploader IDs and author names is not exported.

Hidden sections/modules and any non-empty availability/group restriction are excluded conservatively, including past date windows. No hidden material appears in docs or search. Report inventory lists titles and IDs only.

Policy exclusions (file ID and review reason only; no original filename or content): 16265: Potential personal identifier in original filename; provenance requires review before public redistribution. Entire resource activity withheld.. Policies are course-specific and must not be reused blindly for another course.

Several original attachments carry `allrightsreserved` metadata. Existing teacher attribution in lesson text is preserved. Confirm redistribution rights for teaching documents, examination extracts and third-party images before public distribution. Downloadable originals retain their internal document metadata; this is not a forensic guarantee that all embedded personal data has been removed. Review originals before broad public distribution.

## Conversion details and limitations

Section number and sequence fields control ordering. Duplicate titles use Moodle IDs in filenames. Labels remain inline in ordered section overviews (all Labels in this backup are separators). Page body content is preserved; Moodle's separate Page intro is a course-list description and is not prepended as duplicated lesson text. Resource intros and downloads are retained. Source code is never corrected. Courier paragraphs become fenced C++ blocks; mixed inline code is preserved as inline code. Superscript, subscript, underline, complex tables and lists with nonstandard marker rules retain useful HTML. Empty table headers may be inferred for Markdown tables. Books (when present) use pagenum/subchapter and chapter visibility. Unsupported interactive modules have no placeholder pages.

Broken Moodle references are replaced by visible missing-reference notes, not invented targets. Exact originals are listed below. External URLs are preserved; they can change independently. Remote images remain external and are listed separately. No external assets are downloaded during import.

## Skipped and unsupported activities

| Moodle ID | Type | Title | Reason |
| --- | --- | --- | --- |
| 1076 | forum | Forum aktualności | unsupported: interactive activity; no placeholder exported |
| 1077 | forum | Forum aktualności | hidden |
| 1223 | resource | Podręcznik | hidden |
| 1227 | resource | Zbior zadan z programowania w c++ | hidden |
| 2348 | quiz | test v1 | unsupported: interactive activity; no placeholder exported |
| 1182 | quiz | test v2 | hidden |
| 1213 | quiz | test v3 | hidden |
| 1694 | quiz | test v4 | hidden |
| 1214 | quiz | test v5 | hidden |
| 1185 | quiz | test-poprawiony v6 | hidden |
| 1370 | quiz | algorytmy | hidden |
| 1239 | resource | Prezentacja c++ | hidden |
| 1101 | resource | sprawdzian - if, wstep do c++ WERSJA 1 | hidden |
| 1102 | resource | sprawdzian - if, wstep do c++ WERSJA 2 | hidden |
| 1228 | page | Lista 3 - programy "matematyczne" | hidden |
| 2037 | quiz | Test na ocenę | unsupported: interactive activity; no placeholder exported |
| 2661 | resource | C++_wstęp_v1 | hidden |
| 2668 | resource | C++_wstęp_v2 | hidden |
| 1118 | quiz | Pętle - test treningowy | unsupported: interactive activity; no placeholder exported |
| 1864 | page | Zestawy na kartkowke | hidden |
| 1129 | resource | Losowanie - teoria i przykłady | hidden |
| 1125 | quiz | Funkcje - test na ocenę | hidden |
| 1126 | resource | polecenia | hidden |
| 2575 | resource | funkcje_2f_2020 | hidden |
| 2576 | resource | funkcje 2f_listopad 2020 | hidden |
| 2577 | resource | funkcje_kartkówka | hidden |
| 3206 | page | Zadania - lista 3 | hidden |
| 1895 | resource | Tablice znakowe - rozwiązanie | hidden |
| 3267 | resource | rozwiazanie: zamiana pomiędzy systemami pozycyjnymi na 5 sposobów | hidden |
| 3265 | resource | Zadanie maturalne 1 - szyfr przestawieniowy MOTOR | hidden |
| 3273 | resource | szyfr Vigenera - rozwiazanie 1 | hidden |
| 3274 | resource | szyfr Vigenera - rozwiązanie 2 | hidden |
| 3276 | resource | palindrom cyfrowy i anagramy rozwiazanie | hidden |
| 3316 | resource | rozwiazanie sprawdzianu | publication review: attachment withheld by import policy |
| 3343 | resource | Bisekcja - program | hidden |
| 3344 | resource | Wyszukiwanie binarne program | hidden |
| 3361 | resource | całka - program | hidden |
| 2429 | quiz | pętle_2021 | hidden |
| 1302 | quiz | pętle uzupełnianie | hidden |
| 1304 | quiz | 1f | hidden |
| 1332 | quiz | 1i | hidden |
| 1333 | quiz | 1ia | hidden |
| 1303 | quiz | 1g | hidden |
| 1334 | page | Sprawdziany praktyka | hidden |
| 1336 | quiz | poprawa | hidden |
| 1347 | resource | poprawa_praktyka_2 | hidden |
| 2430 | assign | 21.01.2020 | hidden |
| 2525 | page | Pętle_poprawa 1i | hidden |
| 2545 | resource | poprawa2 | hidden |
| 2585 | resource | Pętle_poprawa | hidden |
| 2717 | resource | 1i_2021 | hidden |
| 2721 | resource | 1f_2021 | hidden |
| 1936 | page | Struktury - przykładowy program i lista zadań | hidden |
| 2297 | page | Struktury z funkcjami składowymi | hidden |
| 2311 | resource | klasa prostokat (bez konstrukorow) | hidden |
| 2316 | page | Klasa paczka - tablice, program zachłanny | hidden |
| 1138 | page | Przykładowe zadania PRAKTYCZNE | hidden |
| 1937 | page | Tablice - zadania trudniejsze | hidden |
| 1141 | resource | Przykładowy całoroczny - z wypieraniem zadań | hidden |
| 2305 | resource | Przykładowy całoroczny - FAJNY | hidden |
| 1450 | resource | sprawdzian ostatniej szansy | hidden |

## Unresolved references

- `03-instrukcja-warunkowa-s664/switch-enum-lista-zadan-4-m3105.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `14-obsluga-plikow-s858/lista-1-pliki-z-jedna-kolumna-m3258.md`: `$@RESOURCEVIEWBYID*2795@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `15-klasa-string-s859/lista-2-szyfrowanie-i-systemy-pozycyjne-m3264.md`: `$@PAGEVIEWBYID*1625@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `15-klasa-string-s859/lista-3-palindromy-palindromy-na-kodach-ascii-cyfrowe-m3266.md`: `$@RESOURCEVIEWBYID*2201@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)
- `15-klasa-string-s859/lista-3-palindromy-palindromy-na-kodach-ascii-cyfrowe-m3266.md`: `$@PAGEVIEWBYID*1625@$` — Target absent from exported course (missing, hidden, restricted, or unsupported)

## External images

None.

## Full ordered course inventory

### 0. WYMAGANIA EDUKACYJNE (section 661)
- `1076` forum: Forum aktualności — unsupported: interactive activity; no placeholder exported
- `1077` forum: Forum aktualności — skipped: hidden
- `1181` resource: Wymagania edukacyjne — converted
- `1223` resource: Podręcznik — skipped: hidden
- `1227` resource: Zbior zadan z programowania w c++ — skipped: hidden
- `3312` resource: bagaż — converted

### 1. Algorytmika - wprowadzenie (section 662)
- `1078` page: Wstęp do algorytmiki - teoria — converted
- `1079` page: Algorytmy liniowe i warunkowe - przykłady — converted
- `1080` page: Algorytmy linowe i warunkowe - lista zadań — converted
- `1081` page: Schematy blokowe - ważne uwagi — converted
- `1083` page: Algorytmy iteracyjne - przykłady — converted
- `1084` page: Algorytmy iteracyjne - lista zadań — converted
- `3100` page: Pseudokod — converted
- `1086` page: Analiza gotowych algorytmów — converted
- `1087` resource: Powtoka - analiza schematow — converted
- `1088` page: Powtorka - rysowanie schematow — converted
- `1089` label: Etykieta — converted
- `2348` quiz: test v1 — unsupported: interactive activity; no placeholder exported
- `1182` quiz: test v2 — skipped: hidden
- `1213` quiz: test v3 — skipped: hidden
- `1694` quiz: test v4 — skipped: hidden
- `1214` quiz: test v5 — skipped: hidden
- `1185` quiz: test-poprawiony v6 — skipped: hidden
- `1370` quiz: algorytmy — skipped: hidden

### 2. Podstawy programowania w C++ (section 663)
- `2617` resource: program wstępny w C++ -> ściągnij i skompiluj — converted
- `1091` page: Język C++ - podstawy — converted
- `1092` page: Podstawy, typy danych - lista zadań 1 — converted
- `1239` resource: Prezentacja c++ — skipped: hidden
- `3101` page: Operatory - lista zadań 2 — converted
- `3133` page: Funkcje matematyczne - wykorzystanie  biblioteki — converted
- `1797` page: C++11/niestandardowe kontrukcje — converted

### 3. Instrukcja warunkowa (section 664)
- `1093` page: Instrukcja warunkowa if - teoria — converted
- `1094` page: if - lista zadań 1 - proste zadania na lekcje — converted
- `1095` page: if - lista zadań 3 — converted
- `1792` page: Podsumowanie wiadomości - if, inkrementacja, dekremantacja, wartość logiczna wyrażenia — converted
- `1099` page: Przykładowe pytania testowe na część testową sprawdzianu z if — converted
- `1100` label: Etykieta — converted
- `3102` page: Instrukcja wyboru switch — converted
- `3103` page: Typ wyliczeniowy — converted
- `3105` page: switch, enum - lista zadań 4 — converted
- `3104` label: Etykieta — converted
- `3144` page: Kody ASCII — converted
- `1101` resource: sprawdzian - if, wstep do c++ WERSJA 1 — skipped: hidden
- `1102` resource: sprawdzian - if, wstep do c++ WERSJA 2 — skipped: hidden
- `1228` page: Lista 3 - programy "matematyczne" — skipped: hidden
- `2037` quiz: Test na ocenę — unsupported: interactive activity; no placeholder exported
- `2661` resource: C++_wstęp_v1 — skipped: hidden
- `2668` resource: C++_wstęp_v2 — skipped: hidden

### 4. Instrukcje iteracyjne (section 670)
- `1105` page: Pęla while, do-while - teoria — converted
- `1106` page: Petla while, do-while - lista 5 — converted
- `1107` page: Pętla for - teoria podstawowa — converted
- `1108` page: Pętla for - lista 6 — converted
- `3107` page: Instrukcja break, continue — converted
- `1863` label: Etykieta — converted
- `1109` page: Pętle różne - lista 7 — converted
- `2695` resource: krótki zestaw powtórzeniowy ze wskazówkami — converted
- `1110` page: Pętle - przykładowe pytania testowe, analiza kodu — converted
- `1118` quiz: Pętle - test treningowy — unsupported: interactive activity; no placeholder exported
- `2106` page: Zadania tekstowe wykorzystujące pętle — converted
- `1864` page: Zestawy na kartkowke — skipped: hidden
- `3108` label: Etykieta — converted
- `1111` resource: Pętla w pętli - teoria — converted
- `1112` page: Pętla w pętli - lista 8 — converted
- `3109` label: Etykieta — converted
- `3313` page: Losowanie - teoria i przykłady — converted
- `1129` resource: Losowanie - teoria i przykłady — skipped: hidden
- `2700` resource: Losowanie - lista 9 — converted

### 5. Funkcje - budowanie własnych podprogramów (section 666)
- `1119` page: Funkcje - teoria — converted
- `1120` resource: Funkcje - krok po kroku z przykładami — converted
- `2792` resource: Funkcje - zadania lista 0 — converted
- `1121` page: Podprogramy - zadania 1 — converted
- `1122` page: Podprogramy - zadania 2 — converted
- `1123` page: Podprogramy - zadania 3 — converted
- `1441` page: przygotowanie do testu — converted
- `3252` page: Teoria funkcje 2 - przeładowanie, funkcje inline — converted
- `1124` label: Etykieta — converted
- `3238` page: Funkcje - algorytmy do realizacji na lekcji — converted
- `1125` quiz: Funkcje - test na ocenę — skipped: hidden
- `1126` resource: polecenia — skipped: hidden
- `2575` resource: funkcje_2f_2020 — skipped: hidden
- `2576` resource: funkcje 2f_listopad 2020 — skipped: hidden
- `2577` resource: funkcje_kartkówka — skipped: hidden

### 6. Tablice statyczne (section 667)
- `1127` page: Tablice - teoria — converted
- `2737` page: Tablica - lista zadań 1a — converted
- `1128` page: Tablice - zadania lista 1 — converted
- `1131` page: Tablice - zadania lista 2 — converted
- `1893` label: Etykieta — converted
- `3205` resource: Schody — converted
- `1132` resource: Przygotowanie do kartkówki z tablic — converted
- `1133` resource: Przygotowanie do kartkówki z tablic - rozwiązanie — converted
- `3206` page: Zadania - lista 3 — skipped: hidden
- `3240` label: Etykieta — converted
- `3239` page: Tablice - algorytmy do realizacji na lekcji — converted

### 7. C++ - zagadnienia teoretyczne (section 669)
- `3211` page: Od pliku źródłowego do wykonywalnego — converted
- `3213` page: Zadania 1 — converted
- `3212` page: Zmienne wskaźnikowe — converted
- `3236` page: Zadania 2 (wskaźniki) — converted

### 8. Dynamiczna alokacja pamięci (section 855)
- `3233` page: Stos a sterta — converted
- `3234` page: Zmienne alokowane dynamicznie — converted
- `3235` page: Tablice dynamiczne — converted

### 9. Tablice dwuwymiarowe (section 854)
- `3220` page: Teoria — converted
- `3222` page: Lista 1 — converted
- `3224` page: Lista 2 — converted
- `3227` label: Etykieta — converted
- `3231` resource: Zadanie temperatury — converted
- `3229` page: Zadanie temperatury - tabelka do wczytania — converted
- `3226` page: Zadanie wypłaty - realizacja algorytmu zachlannego — converted
- `3228` label: Etykieta — converted
- `3230` resource: Zadanie hetman — converted
- `3225` resource: Zadanie piramida — converted
- `3232` resource: hetman - rozwiazanie — converted
- `3296` label: Etykieta — converted
- `3297` resource: Przykładowy sprawdzian — converted

### 10. Algorytmy na liczbach naturalnych (section 864)
- `3367` resource: Dzielniki — converted
- `3370` page: Liczby doskonale — converted
- `3366` resource: Liczby skojarzone  - dzielniki — converted
- `3369` page: Suma cyfr liczby — converted
- `3368` resource: Wesołe liczby — converted

### 11. Rekurencja (section 856)
- `3241` page: Teoria — converted
- `3294` page: Analiza funkcji wypisujacych i odwracających znaki — converted
- `3242` page: Ciągi — converted
- `3244` resource: Zadanie 1 - korale — converted
- `3245` resource: Zadanie 2 - lotto — converted
- `3246` resource: Zadanie 3 - ciąg rekurencyjny (tylko 1.1) — converted
- `3247` resource: Zadanie 4 - ciekawe mnożenia (tylko 3.1 i 3.2) — converted
- `3243` resource: Zadanie 5 - szybkie potęgowanie — converted
- `3248` resource: Zadanie 6 - maturalne, funkcja licz() — converted

### 12. Wstęp do programowania obiektowego (section 857)
- `3249` page: Teoria, czyli krótka opowieść o tym co to klasa a co obiekt — converted
- `3250` page: Przykład 1 - klasa tylko z publicznym dostępem — converted
- `3301` page: Klasa przypominajka — converted
- `3251` page: Przykład 2 - hermetyzacja, konstruktor kopiujący i destruktor — converted
- `3253` page: Przykład 3 - definiowanie funkcji składowych 2 sposób — converted
- `3254` page: Lista 1 — converted
- `3261` page: Przykład 4 - statyczny składnik klasy — converted
- `3255` page: Lista 2 — converted
- `3256` resource: Lista 3 - zadanie — converted
- `3302` page: Podział projektu na 3 pliki — converted
- `3379` page: Obiekt jako pole w innej klasie — converted
- `3380` resource: zadanie domowe - obiekt jako pole innej klasy — converted

### 13. Kontenery (section 860)
- `3319` page: vector teoria i ćwiczenia — converted
- `3317` page: Kontenery — converted
- `3320` page: set teoria i ćwiczenia — converted
- `3321` page: map teoria i ćwiczenia — converted
- `3318` page: Lista zadań vector/set — converted

### 14. Obsługa plików (section 858)
- `3257` page: Przykład - program wzorcowy — converted
- `3258` page: Lista 1 - pliki z jedną kolumną — converted
- `3260` resource: Lista 2 — converted
- `3259` resource: pliki do listy 2 — converted

### 15. Klasa string (section 859)
- `3262` page: Napisy - teoria — converted
- `3263` page: Lista 1 - wykorzystanie metod klasy string — converted
- `1117` label:  — converted
- `1896` page: Przestarzałe tablice znakowe char[] - teoria i zadania — converted
- `1895` resource: Tablice znakowe - rozwiązanie — skipped: hidden
- `3311` label:  — converted
- `3271` page: Szyfrowanie - teoria — converted
- `3264` page: Lista 2 - szyfrowanie i systemy pozycyjne — converted
- `3267` resource: rozwiazanie: zamiana pomiędzy systemami pozycyjnymi na 5 sposobów — skipped: hidden
- `3265` resource: Zadanie maturalne 1 - szyfr przestawieniowy MOTOR — skipped: hidden
- `3270` resource: Zadanie maturalne  - szyfr przestawieniowy iINFORMATYKA — converted
- `3269` label: Etykieta — converted
- `3266` page: Lista 3 - palindromy, palindromy na kodach ASCII, cyfrowe — converted
- `3279` resource: plik do zadania z palindromem na kodach ASCII — converted
- `3268` resource: zadanie genotyp — converted
- `3272` page: Lista 4 - anagramy — converted
- `3273` resource: szyfr Vigenera - rozwiazanie 1 — skipped: hidden
- `3274` resource: szyfr Vigenera - rozwiązanie 2 — skipped: hidden
- `3276` resource: palindrom cyfrowy i anagramy rozwiazanie — skipped: hidden
- `3275` resource: Zadanie maturalne 3 - palindrom z przesunięciem — converted
- `3277` resource: Zadanie maturalne 4 - Wega — converted
- `3278` resource: sygnały - plik do zadania Wega — converted
- `3281` label: Etykieta — converted
- `3280` page: Lista 5 — converted
- `3282` resource: pliki TROJKOWE.txt i ABC.txt — converted
- `3316` resource: rozwiazanie sprawdzianu — skipped: publication review: attachment withheld by import policy

### 16. Złożoność obliczeniowa (section 671)
- `3329` page: Teoria — converted
- `3330` page: Jak wyznaczyć liczbę operacji dominujących — converted
- `3332` page: Lista algorytmów — converted
- `3331` resource: Zadania — converted
- `3346` resource: Zadanie maturalne potęgi maj 2008 — converted
- `3347` resource: Zadanie maturalne prostokąty maj 2017 — converted
- `3348` resource: Zadanie maturalne liczby osiągalne maj 2012 — converted

### 17. Algorytmy (section 861)
- `3340` page: Bisekcja — converted
- `3342` resource: Bisekcja - zadanie maturalne — converted
- `3343` resource: Bisekcja - program — skipped: hidden
- `3341` page: Wyszukiwanie binarne — converted
- `3344` resource: Wyszukiwanie binarne program — skipped: hidden

### 18. Algorytmy (section 862)
- `3351` page: Schemat Hornera — converted
- `3352` resource: Zamiana sys liczbowych ze schematem Hornera — converted
- `3353` resource: Podzielność - zad matur — converted
- `3354` resource: Schemat Hornera i zamiana sys liczbowych — converted

### 19. Algorytmy - całka numeryczna (section 863)
- `3359` page: Całka numeryczna — converted
- `3361` resource: całka - program — skipped: hidden
- `3360` resource: zadanie figura - maturalne — converted

### 20. Instrukcje iteracyjne - testy, pętla w pętli (section 665) — skipped: hidden
- `2429` quiz: pętle_2021 — skipped: hidden
- `1302` quiz: pętle uzupełnianie — skipped: hidden
- `1304` quiz: 1f — skipped: hidden
- `1332` quiz: 1i — skipped: hidden
- `1333` quiz: 1ia — skipped: hidden
- `1303` quiz: 1g — skipped: hidden
- `1334` page: Sprawdziany praktyka — skipped: hidden
- `1336` quiz: poprawa — skipped: hidden
- `1347` resource: poprawa_praktyka_2 — skipped: hidden
- `2430` assign: 21.01.2020 — skipped: hidden
- `2525` page: Pętle_poprawa 1i — skipped: hidden
- `2545` resource: poprawa2 — skipped: hidden
- `2585` resource: Pętle_poprawa — skipped: hidden
- `2717` resource: 1i_2021 — skipped: hidden
- `2721` resource: 1f_2021 — skipped: hidden

### 21. Pierwsze przymiarki do programowania obiektowego (section 770) — skipped: hidden
- `1936` page: Struktury - przykładowy program i lista zadań — skipped: hidden
- `2297` page: Struktury z funkcjami składowymi — skipped: hidden
- `2311` resource: klasa prostokat (bez konstrukorow) — skipped: hidden
- `2316` page: Klasa paczka - tablice, program zachłanny — skipped: hidden

### 22. Przygotowanie do sprawdzianu całościowego (section 668) — skipped: hidden
- `1138` page: Przykładowe zadania PRAKTYCZNE — skipped: hidden
- `1937` page: Tablice - zadania trudniejsze — skipped: hidden
- `1141` resource: Przykładowy całoroczny - z wypieraniem zadań — skipped: hidden
- `2305` resource: Przykładowy całoroczny - FAJNY — skipped: hidden
- `1450` resource: sprawdzian ostatniej szansy — skipped: hidden

