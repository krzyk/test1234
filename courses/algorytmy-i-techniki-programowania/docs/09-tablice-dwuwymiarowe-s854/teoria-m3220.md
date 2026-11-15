# Teoria

### Tablica dwuwymiarowa - podstawy

Tablica dwuwymiarowa to tablica, której elementami są tablice.

**Deklaracja tablicy dwuwymiarowej**

```cpp
typ nazwa [liczba wierszy] [liczba kolumn];
```

np. stworzenie dwuwymiarowej tablicy liczb całkowitych o nazwie tab, w sumie 100 komórek: 3x2:

```cpp
int tab [ 3 ][ 2 ];
```

Wartości początkowe tablicy możemy nadać przy jej deklaracji np.

```cpp
int tab[3][2] = {{1,3},{4,5},{0,-1}};
```

Przy nadawaniu wartości tablicy można pominąć wartość w pierwszym nawiasie kwadratowym:

```cpp
int tab[][2] = {{1,3},{4,5},{0,-1}};
```

**Odwoływanie się do elementów tablicy**

tab[0][0] - pierwszy element tablicy tab

`tab[0][0]=7;`  //przypisanie wartości do pierwszego elementu, [0][0] - indeksy pierwszego element tablicy

tab[2][1] - ostatni element tablicy (zadeklarowanej int tab[3][2]) bo tablica numerowana jest od zera

### **Podstawowe operacje na tablicach**

**Wczytanie elementów do tablicy:**

```cpp
for(int i=0;i<3;i++)
   for(int j=0;j<2;j++){
         cout << "podaj element tablicy o indeksach" <<i<<","<<j;
         cin >> tab[i][j];
    }
```

**Wylosowanie elementów do tablicy:**

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
int main(){
  srand(time(NULL));
  
  for(int i=0;i<3;i++)
    for(int j=0;j<2;j++)
       tab[i][j]=rand()%10; //losowanie liczb jednocyfrowych
   return 0;
}
```

**Wypisanie tablicy**

```cpp
for(int i=0;i<3;i++){
   for(int j=0;j<2;j++)
       cout <<   tab[i][j];
     cout << endl;  //przejście do nowej linii po wypisaniu wiersza
    }
```

### Tablice i funkcje

Funkcja przyjmująca jako parametr tablicę - najprostsze podejście

```cpp
void funkcja(int tablica[3][2]){
    //.....
}
int main(){
     int tab[3][2];
     //....
     funkcja(tab); //wywolanie funkcji, nie trzeba podawać rozmiaru, przekazujemy samą nazwę
}
```
