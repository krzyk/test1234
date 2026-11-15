# Tablice - teoria

**Tablica** - zbiór uporządkowanych danych takiego samego typu, w którym poszczególne elementy dostępne są za pomocą indeksu. Indeks przyjmuje wartości numeryczne od `0` do `(rozmiarTablicy - 1)`.  
Tablica należy do<u> typów danych złożonych.</u>

<u>Tablice statyczne, o których mowa w tym dziale są przechowywane a pamięci operacyjnej w obszarze nazywanym STOSEM (ang. stack). Wielkość pamięci zarezerwowanej na stosie jest dokładnie określoną w momencie kompilacji programu i dlatego też nie zmienia się (statyczna alokacja pamięci)</u>

Przyklad:

```cpp
int tab[5];
```

- Jest to deklaracja tablicy 5-cio elementowej typu całkowitego.
- Elementy tablicy numerowane są od zera, zatem ta tablica ma elementy tab[0], tab[1], tab[2], tab[3], tab[4];
- Przykładowa zawartość tablicy to: 5 6 0 5 -2
- Tablice numerowane/indeksowane są od zera, zatem wartość 5 jest na pozycji 0 oraz 3

**Wypełnienie tablicy:**

1. Po elemencie:

```cpp
tab[0]=5;
tab[1]=4;
tab[2]=7;
```

- ta tablica ma wartości: 5,4,7
- 5 jest pierwszym elementem tablicy, jej indeks to 0
- takie wypełnianie tablic nie jest zbyt efektywne

2. Z pętlą `for`

```cpp
for(int i=0;i<3;i++){
     cout << "podaj element tablicy o indeksie "<< i <<end;
     cin >>  tab[i];
}
```

3. Wylosowanie dowolnych elementów do tablicy

```cpp
for(int i=0;i<3;i++){
    tab[i]=rand();
}
```

4. Deklaracja i wypełnienie tablicy - inicjalizacja:

```cpp
int tablica[5]={4,5,6,2,3};
int tablica[5]={4,5}; //w tym przypadku pozostałe elementy zostaną wypełnione zerami
```

lub bez podawania rozmiarów:

```cpp
int tablica[]={4,5,6,2,3};
```

lub w stylu C++11:  
`int tablica[]{4,5,6,2,3};`

Poniższy zapis wypełnia całą tablice elementami domyślnymi (0 dla typów całkowitych)

```cpp
int tablica[100]={};
```

**Wypisanie elementów tablicy:**

Tablicę należy wypisać po elemencie - koniecznie należy użyć pętli for

```cpp
for(int i=0;i<3;i++) cout << tab[i] << " ";
```

**Początkowe wartości tablicy** - co znajduje się w tablicy jeśli nie przypiszemy jej od razu żadnych danych?

```cpp
int tablica[10];
```

1. Jeżeli tablica jest inicjowana (deklarowana) w programie głównym (tj. wewnątrz funkcji main()) to wówczas kompilator nie inicjuje jej wartości początkowych, elementy pozostają nieokreślone
2. Jeśli tablica jest inicjowana bezpośrednio w przestrzeni nazw (poza main()) to elementom tablicy automatycznie przypisane zostaną wartości domyślne (0 lub "")
