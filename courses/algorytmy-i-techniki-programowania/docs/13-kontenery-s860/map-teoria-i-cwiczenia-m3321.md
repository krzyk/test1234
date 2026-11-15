# map teoria i ćwiczenia

map to kontener z C++ Standard Library, który przechowuje dane w postaci **par: klucz → wartość.** Mapy, podobnie jak sety nie posiadają indeksów. Indeksowanie odbywa się na podstawie unikalnego klucza. Kluczem nie musi być liczba, zazwyczaj jest to np. string. Takim kluczem może być np. pesel, a wartością nazwisko.

Najważniejsze cechy &lt;map&gt;:

- klucze są unikalne
- dane są posortowane automatycznie wg klucza
- map zapewnię bardzo szybkie wyszukiwanie danych

```cpp
#include<map>
map<string,int> m;  //deklaracja mapy

m["Ala"] = 17;
m["Bartek"] = 18;
```

Każdy element mapy to obiekt: pair&lt;klucz, wartość&gt;.  Przykładowo, dla takiej deklaracji mapy:  
map&lt;string,int&gt; m;  
możemy przypisać:  
m["Ala"] = 17;  
i wówczas w mapie przechowywana jest para `("Ala", 17).`

Wypisanie mapy:

```cpp
for(auto element : m){
    cout << element.first << " " << element.second << endl;
}
```

`first` - zwraca bieżący klucz  
`second` - zwraca bieżącą wartość

Przykładowe funkcje:

- `insert ()` - dodawania elementów,np.: `m.insert({"Jan",20}); lub m["Jan"]=20;`
- `find() - sprawdzenie, czy istnieje klucz: m.find("Ala") != m.end()`
- `erase() - usunięcie elementu, np: m.erase("Ala");`
- `size() - rozmiar mapy`
- `empty() - sprawdzanie czy mapa jest pusta`

```cpp
Ćwiczenia:
```

1. Stwórz słownik, w którym będziesz przechowywał 5 stolic i państw azjatyckich. Dodawaj elementy metodą insert oraz zwykłym dodawaniem po kluczu. Wypisz zawartość mapy na ekran.
2. Wczytaj n liczb i policz ile razy wystąpiła każda liczba.
3. Wczytaj słowo i policz ile razy wystąpiła w nim każda litera
