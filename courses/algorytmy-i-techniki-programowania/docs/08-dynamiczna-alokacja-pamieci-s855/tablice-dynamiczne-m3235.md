# Tablice dynamiczne

**Statyczna tablica jednowymiarowa**

```cpp
int tab[5]={1,2,3,4,5};
```

**Tablica dynamiczna jednowymiarowa**

```cpp
int *tab=new int[n];
// .... operacje na tablicy
delete [] tab; //UWAGA! Koniecznie zwolnienie pamięci na stercie!
```

`int* tab2 = new int[5]();` // Inicjalizacja domyślna (wartością zero). Tworzy tablicę 5 intów, każdy = 0  
`int* tab3 = new int[5]{1, 2, 3};` // Inicjalizacja listą. Inicjalizuje: 1, 2, 3, 0, 0

```cpp
delete [] tab2;
delete [] tab3;
```

Więcej o dynamicznych tablicach, także dwuwymiarowych znajdziesz tutaj: <https://www.p-programowanie.pl/cpp/tablice-dynamiczne>

---

<a id="yui_3_13_0_2_1538578251199_411"></a>

**Zadania**

<ol><ol>
<li>Zadeklaruj w sposób statyczny tablicę jednowymiarową o liczbie elementów równej 10mln. Czy program się kompiluje? (zwróć uwagę na to co zwraca funkcja main()). Zmień kod tak, aby deklaracja tak dużej tablicy była możliwa.</li>
<li>Użytkownik podaje ile elementów wczyta do tablicy, następnie wypełnia z klawiatury tablicę (dynamiczna alokacja tablicy - bo dopiero użytkownik decyduje o jej rozmiarze)</li>
<ul>
<li style="list-style-type: none;">
<ul>
<a id="yui_3_13_0_2_1538578251199_417"></a><li>program zlicza ile w tablicy jest wartości ujemnych</li>
<li>program przepisuje do tablicy ujemne[] te wartości, które są ujemne (rozmiar tablicy ujemne[] zależy od liczby elementów ujemnych, zatem dynamiczna alkocja tej tablicy)</li>
</ul>
</li>
</ul>
</ol></ol>

---

## Tablice i funkcje

#### Tablica parametrem funkcji

```cpp
void wypelnij(int t[], int n) {
for(int i=0; i<n; i++)
tab[i] = i * i; // Przykładowe wypełnienie tablicy
}
int main(){
....
}
```

#### Funkcja zwracająca tablicę

```cpp
#include <iostream>
int* stworzTablice(int n) {
     int* tab = new int[n]; // Dynamicznie alokowana tablica
     for (int i = 0; i < n; ++i) 
       tab[i] = i * i; // Przykładowe wypełnienie tablicy

return tab; // Zwracamy wskaźnik na tablicę
}
int main() {
int n= 5;
int* tablica = stworzTablice(n);
// Wyświetlamy zawartość tablicy
for (int i = 0; i < n; ++i) {
    cout << tablica[i] << " ";
}
delete[] tablica; 
}
```

---

1. Napisz program, który tworzy funkcję zwracającą tablicę. Funkcji przekazujesz rozmiar tablicy oraz liczbę, jej zadaniem będzie zwrócenie tablicy która zawiera kolejne wielokrotności podanej liczby. Przykładowo dla funkcja(5, 2) -&gt; otrzymuje 5-elementowa tablice z kolejnymi wielokrotnościami dwójki, czyli: 2,4,6,8,10
2. Napisz funkcję która zwraca tablicę będącą zapisem dwójkowym liczby podanej jako argument funkcji.
3. Korzystając z powyższego linka lub [tego](http://www.algorytm.edu.pl/tablice-w-c/tablice-wielowymiarowe.html) stwórz dwuwymiarową tablicę i wpisz do niej losowe liczby symulujące rzut kostką.
4. *\*\*\*\*(dla chętnych)* Stwórz tablicę dwuwymiarową o zmiennej liczbie elementów, taką że w 1 wierszu będzie ona zawierała 1 element, w drugim dwa, w trzecim 3 itd (aż do rozmiaru n=5). Wypełnij tablicę losowymi liczbami.
