# set teoria i ćwiczenia

Kontener set (zbiór) to kontener STL który przechowuje unikalne (niepowtarzające się) elementy w sposób uporządkowany. Charakterystyczne cechy:

- brak duplikatów
- automatycznie posortowane dane w sposób rosnący
- w set nie ma indeksów - elementy są identyfikowane tylko po wartościach

Składnia:

<a id="code-block-viewer"></a>

`#include <set>`  
`using namespace std;`  
  
`set<int> s;`

Podstawowe funkcje:

- `insert(element)` - dodanie elementu
- `erase(element)`  - usuniecie elementu;
- `find(element)` - szuka element
- `size()` - rozmiar set
- `count()` - zlicza elementy w zbiorze, np. zbiór.count(x) - sprawdza czy x znajduje się w zbiór)
- `empty()` - sprawdzanie czy pusty
- iteratory `begin(), end()`

Zamiana vectora na set:

```cpp
vector<int> v = {1,2,2,3,4};
set<int> s(v.begin(), v.end());
```

Przydatne porównanie:

```cpp
if(tab.find(x) != tab.end())
```

- sprawdzenie, czy x znajduje się w zbiorze tab. Jeżeli funkcja find() znajdzie jakiś element w zbiorze, to zwróci jej iterator, ale jeśli nie znajdzie, to zwróci tab.`end()` co oznacza iterator za ostatnim elementem zbioru.  
Dlatego też if(tab.find(x) != tab.end())  sprawdza, czy element x jest w zbiorze. 

---

Ćwiczenia:

1. Wylosuj 10 liczb jednocyfrowych dodatnich do vectora, a następnie wykorzystując set sprawdź ile jest wśród nich unikalnych liczb. Wypisz unikaty na ekran.
2. Wczytaj 10 znaków do vectora. Przepisz je do set. Wypisz elementy, które się powtórzyły.
3. W grze Lotto podczas każdego losowania maszyna losująca wybiera 6 liczb z zakresu od 1 do 49. Zasymuluj grę w lotto:

   - wylosuj 6 liczb, zapisz je w odpowiednim kontenerze - pamiętaj, aby się nie powtarzały
   - następnie spróbuj wylosować wielokrotnie 6 liczb i sprawdź za którym razem trafiono trójkę (trafiono 3 liczby z 6), 4, 5, 6.
