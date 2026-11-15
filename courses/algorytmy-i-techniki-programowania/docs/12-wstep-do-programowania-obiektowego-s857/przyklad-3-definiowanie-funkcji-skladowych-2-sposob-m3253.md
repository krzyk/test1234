# Przykład 3 - definiowanie funkcji składowych 2 sposób

**Pierwszy sposób:** funkcję definiujemy wewnątrz definicji klasy (wewnątrz class{ .... }) - patrz przykład 1 i 2. Funkcja zdefiniowana wewnątrz klasy jest domyślnie funkcją typu inline

**Drugi sposób:**w definicji klasy umieszcza się tylko samą deklarację, natomiast jej definicję (czyli ciało) piszemy poza ciałem klasy:

`class Tpralka{`  
 `string model;`  
 `int cena;`  
  
 `public:`  
 `void wypisz();`  //sama deklaracja  
 `void zapamiętaj(string m, int c); //sama deklaracja`  
`} ////////////////koniec definicji klasy`

```cpp
void Tpralka::wypisz(){
      cout<<"Jestem pralką o modelu<<model;      //a poza klasa pełna definicja
}

void Tpralka::zapamiętaj(string m, int c){
        model=m;
          cena=c;          
}
```

Uwaga!  
:: to tzw. operator zakresu. Zwróć uwagę na kolejność definicji funkcji składowej w sytuacji kiedy definiujemy ją poza klasą:

*typ\_funkcji **nazwa\_klasy** :: <u>nazwa\_funkcji</u>* czyli: *void **Tpralka** :: <u>wypisz()</u>*

**Trzeci sposób - złożony projekt:**

1. Definicję klasy umieszczamy w pliku nagłówkowym o nazwach np. Tpralka.h
2. Nowa klasa = nowy plik
3. Definicję dużych funkcji składowych (czyli takich, które lepiej tworzyć poza ciałem klasy) umieszczamy w pliku źródłowym np. o nazwie Tpralka.cpp

//plik nagłówkowy **Tpralka.h**  
`class Tpralka{`  
 `//pola klasy`  
 `//małe funkcje składowe`  
`}`

//plik **Tpralka.cpp:**  
**`#include "Tpralka.h"`**  
`//definicje pozostałych funkcji składowych`  
`int main(){ //main może być tez w kolejnym, innym pliku o rozszerzeniu cpp`  
`.......`  
`}`
