# Napisy - teoria

Operacje na napisach w C++ opisane poniżej są możliwe po podłączeniu biblioteki string (**#include&lt;string&gt;**) Biblioteka ta jest biblioteką **obiektową**, dlatego **zmienne typu string** będziemy nazywać **obiektami klasy string.**

Na obiektach klasy string - czyli na napisach - możemy działać różnymi metodami. Metody działają podobnie jak funkcje, ale nazywamy je metodami bo wywołujemy je na konkretnym obiekcie klasy string, tzn.:

```cpp
string napis = "Ala";
int dlugosc = napis.size();
```

W podanym przykładzie na obiekcie `napis` została wywołana metoda `size()` która zlicza liczbę znaków w napisie.

Ogólnie możemy zapisać, że metody wywołujemy w następujący sposób:

```cpp
napis.metoda(parametry);
```

## Przykładowe metody:

- `size(), length()` - metody, które zwracają liczbę znaków danego łańcucha
- `empty()` - sprawdza, czy napis jest pusty (zwraca wartość true lub false), np: `if(napis.empty())` zwróci wartość true, jeśli napis jest pusty
- `clear()` - usuwa wszystkie znaki z napisu
- `find("szukany_tekst")` - sprawdza, czy `"szukany_tekst"` znajduje się w przeszukiwanym łańcuchu znaków. Jeśli go znajdzie zwróci indeks pierwszego znaku szukanego tekstu. Jeśli nie, zwróci -1 np.: `string napis = "AlaMaKota"; cout<<napis.find("Ma"); //wypisze 3`
- `substr(start, liczba)` - metoda, która zwraca `liczba` znaków ciągu począwszy od znaku o indeksie `start, np.: string napis = "AlaMaKota"; cout<<napis.substr(3,2); //wypisze Ma`
- `replace(start, ile, "inny") - metoda, która zamienia wybrany ciąg znaków w łańcuchu(począwszy od indeksu start dokładnie liczba znaków, na "inny") np.: string napis = "AlaMaKota"; cout<<napis.replace(5,4,"Psa"); //wypisze AlaMaPsa`
- `at(indeks)- zwraca znak znajdujący się na pozycji indeks, np. cout<<napis.at(3) //wypisze M`

## Ponadto w klasie string przedefiniowano (przeciążono) operatory:

- operator + dla napisów - łączy napisy
- operator przypisania = przypisuje cały napis mimo, że nie jest to typ prosty
- operatory porównywania == oraz != porównują napisy

## Napisy i tablice:

Każdy napis jest także tablicą jednowymiarową, zatem:

- `cout<< napis[0];` //wypisze pierwszą litere napisu
- `for(int i=0;i<napis.size();i++) cout<< napis[i]<<endl`; // wypisze napis po literze, każda w nowej linii
- itd :)

**Obsługa napisów:**Skoro napis jest tablicą, a z drugiej strony ma do dyspozycji wiele metod, to większość zadań można zrobić na kilka sposobów np: na wypisanie pierwszej litery napisu mamy następujące sposoby:

- `cout<< napis[0];`
- `cout<< napis.at(0);`
- `cout<< napis.substr(0,1);`

Czytaj więcej:

- <https://www.cppreference.com/w/cpp/string/basic_string_view.html#Member_functions>
- <http://pl.wikibooks.org/wiki/C++/String>
