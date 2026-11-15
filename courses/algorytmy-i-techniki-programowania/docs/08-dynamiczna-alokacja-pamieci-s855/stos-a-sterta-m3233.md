# Stos a sterta

**Stos, sterta - część pamięci wirtualnej przydzielonej programowi podczas uruchomienia.**

---

**Stos (*ang. stack*)**

1. **Sposób działania**: Stos działa na zasadzie LIFO (**Last In, First Out**), co oznacza, że ostatnio dodane dane są pierwsze do usunięcia. Jest to stosowane do zarządzania pamięcią dla zmiennych lokalnych i wywołań funkcji.
2. **Alokacja**: Pamięć na stosie jest zarządzana automatycznie. Kiedy funkcja jest wywoływana, zmienne lokalne i parametry są umieszczane na stosie. Po zakończeniu funkcji pamięć jest automatycznie zwalniana.
3. **Rozmiar**: Stos ma ograniczony rozmiar, który jest z góry określony w momencie uruchomienia programu (zwykle kilkaset KB do kilku MB). Przekroczenie tego limitu prowadzi do błędu zwanego **stack overflow**.
4. **Szybkość**: Operacje na stosie są szybkie, ponieważ alokacja i zwalnianie pamięci odbywają się w sposób automatyczny i bezpośredni (przesuwanie wskaźnika stosu).

Na stosie przechowywane są np. zmienne lokalne, tablice statyczne, adresy powrotu (np. przy rekurencji), argumenty wywołania funkcji, wartości zwracane przez funkcje.

Przykładowo, deklarując zmienną, wpada ona na stos i jest tam tak długo, jak ją potrzebujemy (czyli w obrębie funkcji, nawiasów {} itd). Nie musimy dbać o jej zdejmowanie ze stosu, wszystko dzieje się w tle, poza nami.

Ideę stosu danych można zilustrować jako stos położonych jedna na drugiej książek – nowy egzemplarz kładzie się na wierzch stosu i z wierzchu stosu zdejmuje się kolejne egzemplarze. Elementy stosu poniżej wierzchołka można wyłącznie obejrzeć, aby je ściągnąć, trzeba najpierw po kolei ściągnąć to, co jest nad nimi<sup>1</sup>.   
  
UWAGA! Kolejne komórki tablic deklarowanych statycznie są zapisywane w pamięci obok siebie, dzięki czemu tablice statyczne działają szybciej niż te dynamiczne.

## 

---

**Sterta (kopiec, stóg, *ang. heap*)**

### 

1. **Sposób działania**: Sterta to bardziej elastyczna przestrzeń pamięci, która nie stosuje zasady LIFO. Można dynamicznie alokować i zwalniać pamięć w dowolnym momencie w trakcie działania programu.
2. **Alokacja**: Pamięć na stercie jest zarządzana ręcznie przez programistę. W C++ używa się operatorów **`new`** do alokacji i **`delete`** do zwalniania pamięci. Programista musi sam dbać o zwalnianie pamięci, aby uniknąć wycieków pamięci.
3. **Rozmiar**: Sterta może być bardzo duża, a jej rozmiar ograniczony jest tylko przez dostępne zasoby systemowe. Pozwala na dynamiczną alokację pamięci o zmiennym rozmiarze.
4. **Szybkość**: Operacje na stercie są wolniejsze niż na stosie, ponieważ system operacyjny musi szukać odpowiedniego bloku pamięci do przydzielenia. Dodatkowo, ręczne zarządzanie pamięcią przez programistę jest bardziej skomplikowane.

Na stercie z kolei są przechowywane dynamiczne struktury danych (w C++ to np. tablice definiowane za pomocą słowa kluczowego new, klasy i obiekty) i inne dynamiczne przedzielane obszary pamięci.   
  
Na stercie pamięć przydzielana jest dynamicznie, w ramach rozszerzenia się np. tablicy (w trakcie działania już programu, gdzie nie jest znany rozmiar tablicy i tablica rośnie w ramach potrzeb) Programista musi jednak pamiętać o zwolnieniu pamięci (delete w C++), aby nie doprowadzić do tzw. wycieku danych (*ang. heap overflow*).

Kolejne komórki tablicy w pamięci nie są rezerwowane obok siebie!

**Kiedy lepiej pracować na stercie (używając dynamicznej alokacji pamięci np. w tablicach)?**

<ol>
<li style="list-style-type: none;"><ol>
<li style="text-align: left;">Kiedy potrzebujemy dużo pamięci (np. dla dużych rozmiarów tablicy). Rozmiar stosu to zazwyczaj ok. 1MB, więc jeśli potrzebujemy coś więcej możemy ryzykować tzw. przepełnienie stosu (<em>ang. stack overflow</em>)</li>
<li style="text-align: left;">Kiedy budujemy struktury (tablice, listy), których nie znamy początkowo rozmiarów (ich wielkość jest podawana np. z klawatury), a istnieje szansa że mogą "znacznie urosnąć"</li>
<li style="text-align: left;">Kiedy sami chcemy mieć wpływ jak długo dana wartość będzie w programie zapamiętana (np. poza funkcją) gdyż sami decydujemy o zwalnianiu przydzielonej pamięci</li>
<li style="text-align: left;">Kiedy nie zależy nam jednocześnie na czasie (sterta działa wolniej!)</li>
</ol></li>
</ol>

1 [za wikipedia]
