# Lista 2

1. Wylosuj dowolne liczby do tablicy kwadratowej, tj. o rozmiarze 5x5, a następnie:
   1. wyznacz minimalny element w całej tablicy (uwaga: początkowa wartość minimalna powinna być wartością znajdującą się w tablicy, np. min=tab[0][0])
   2. wyznacz sumę elementów znajdujących się na przekątnej macierzy (tablicy)
   3. policz, ile znajduje się zer nad przekątną (zadanie rozwiąż w sposób nieoptymalny-if oraz optymalny - bez użycia instrukcji warunkowej)
   4. wyznacz średnią elementów pod przekątną (w sposób optymalny)
2. Utwórz tablicę dwuwymiarową 3x5 i wypełnij ją liczbami będącymi sumą indeksów danej komórki tablicy. Następnie:
   1. usuń dowolny wiersz (jego indeks wczytaj z klawiatury) i jednocześnie przesuń pozostałe wiersze w górę; ostatni wiersz wypełnij zerami
   2. podpunkt 1) zrealizuj  w funkcji, która jako argument będzie pobierała tablicę oraz indeks wiersza, który ma być usunięty
   3. rozwiń funkcję z podpunktu 2) aby pobierała dodatkowo 3 argument - informację, czy wpisany indeks dotyczy usunięcia wiersza lub kolumny (i odpowiednio skonstruuj ta funkcję aby można było za jej pomocą kasować wiersze i kolumny)
3. Wypełnij tablicę dwuwymiarową kwadratową stopnia 10 losowo wartościami 0 lub 1. Wypisz tablicę oraz:

   1. Zsumuj liczby na przekątnej pierwszej i na przekątnej drugiej
   2. Podaj, ile jest wierszy składających się z dokładnie dwóch niepustych bloków: pierwszego składającego się samych zer i drugiego składającego się z samych jedynek.

   **Przykład:**

   Dla zestawu danych:

   100010000100

   000000111111

   000000000000

   111111111100

   Mamy jeden taki wiersz o indeksie 1

   3. Podaj długość najdłuższego bloku złożonego z samych zer pojawiającego się w wierszach oraz numery wierszy w których się znajduje.

   **Przykład:**

   Dla zestawu wierszy:

   10001**0000**10

   00111111111

   00011111101

   1100111**0000**

   **0000**1111100

   Wynikami są liczba 4 (długość najdłuższego bloku) oraz numery wierszy 0, 3, 4.
4. Stwórz dwie tablice dwuwymiarowe 6x6. Następnie:
   1. pierwszą tablicę wypełnij losowymi liczbami całkowitymi z przedziału (-10, 10).
   2. do drugiej tablicy wpisz sumę liczby, która znajduje się w danej komórce pierwszej tablicy i wszystkich liczb sąsiadujących (nad, pod i obok - pomiń te po przekątnej), uwzględnij przy tym tzw. periodyczne warunki brzegowe, tzn. komórka o indeksie (0,0) ma także 4 sąsiadów - jej sąsiad z lewej to (0,3) a z góry to (3,0).  
      Podpowiedź: do periodycznych warunków brzegów użyj operatora %
5. *Model Isinga.* W fizyce tablice dwuwymiarowe mogą służyć do modelowania zachowania ferromagnetyka. Idea polega na tym aby w każdej komórce tabeli umieścić spiny, które mogą przyjmować wartości +1 (spin w górę) lub -1 (spin w dół). Skonstruuj taki model dla tablicy dwuwymiarowej 10x10 i umieść w niej losowo spiny.  
   Przykład: dla tablicy 4x4:  
   1   -1    1    1  
   -1   1   -1    1  
   1    1   -1   -1  
   -1   -1   1    1  
   Następnie oblicz:
   1. Namagnesowanie magnetyka - czyli sumę wszystkich spinów podzieloną przez ich liczbę
   2. Energię ferromagnetyka, liczoną jako sumę iloczynów najbliżej sąsiadujących spinów, np. zaczynając od spinu o indeksie (1,1) mamy: 1\*(-1) + 1\*(-1) + 1\*(-1) + 1\*1    (zadany spin mnożymy ze spinem z prawej, z lewej, z góry, z dołu). I tak dla każdego spinu.  
      UWAGA! Uwzglednij periodyczne warunki brzegowe
