# Zmienne wskaźnikowe

**Wskaźnik** - **zmienna przechowująca adres (zmienna wskazująca na adres) innej zmiennej.**

**\***     -   operator deferencji

**&**    -   operator adresu

---

`int *x;` //deklaracja zmiennej wskaźnikowej

`int y=8;`   
`x=&y;` //wskaźnik x będzie od teraz wskazywał na adres zmiennej y  
`cout<<*x;` //wypisze wartość zmiennej y, bo x przekazaliśmy adres zmiennej y.  
`cout<<x;` //wypisze adres zmiennej y, bo wskaźnik x przechowuje adres zmiennej y

`*x=10;` //ustawienie nowej wartości  
cout&lt;&lt;y; //korzystając ze wskaźnika i operatora deferencji \* zmieniliśmy wartość, która siedziała pod adresem x, a ponieważ wskazywała ona na to co przechowuje y, zmieniła się wartość y

`int b=*x;` //przepisanie wartości zmiennej x do zwykłej zmiennej b

`*x++;` //taka instrukcja modyfikuje wartość zmiennej, na którą wskazuje wskaźnik, y=11;

`x++;` //tu modyfikujemy wartość wskaźnika, czyli adresu zwiększając tę wartość o tyle bajtów, ile zajmuje zmienna na którą wskaźnik wskazuje (dla int może to być 4 bajty)

---

**Wskaźniki a tablice**

`int tab[]={2, 5, 9};`  
`cout<<tab;` //adres pierwszego elementu tablicy   
`cout<<tab+1;` //adres drugiego elementu tablicy  
  
`cout<<*tab;` //operator \* wyciąga wartość, jaka kryje się pod adresem tab, czyli pod adresem pierwszego elementu tablicy  
`cout<<*(tab+1);` //wypisze element o indeksie 1 (jego wartość)

---

---

**Przekazywanie argumentów funkcji moze odbywać się poprzez:**

1. **Wartość (klasyczna funkcja)**  
   `int dodaj(int x){`  
    `x=x+5`  
   `}`  
   `main(){`  
   `int a = 10;`  
   `dodaj(a);`  
   `cout<<a;`//a=10 po wyjsciu z funkcji a **nie zmieni wartości**, bo funkcja pracuje na lokalnych zmiennych, których wartości są kopiami argumentów funkcji
2. **Referencję**  
   `int dodaj(int &x){`  
    `x=x+5`  
   `}`  
   `main(){`  
   `int a = 10;`  
   `dodaj(a);`  
   `cout<<a;`//a=15 bo pobrany został adres zmiennej, funkcja działa bezpośrednio na zmiennej a nie na jej kopii
3. **Wskaźnik**  
   `int dodaj(int *x){ //argument to wskaźnik na zmienną, czyli funkcja pobiera adres`  
    `*x=*x+5`  
   `}`  
   `main(){`  
   `int a = 10;`  
   `int *wsk;`  
   `wsk=&a;`  
   `dodaj(wsk);`  
   `cout<<a;`//a=15 bo funkcja poprzez wskaźnik działa bezpośrednio na zmiennej  a nie na jej kopii

---

Uwaga! Istnieje taka umowa (we wcześniejszych wersjach C++), że jeżeli wskaźnik na nic nie pokazuje, to adres na który wskazuje wynosi 0 (NULL). W C++11 wprowadzono jednakżę stałą `nullptr`, która oznacza adres zerowy.
