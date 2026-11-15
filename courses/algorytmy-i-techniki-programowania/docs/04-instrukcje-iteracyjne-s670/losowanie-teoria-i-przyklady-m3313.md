# Losowanie - teoria i przykłady

**Generowanie liczb pseudolosowych**

Do generowania liczb losowych służy funkcja rand(). Generuje ona losową liczbę całkowitą między 0 i RAND\_MAX (stała zdefiniowana w bibliotece cstdlib) .

Aby wykorzystać funkcję rand() trzeba:

1. Dołączyć bibliotekę cstdlib do programu
2. Wywołać funkcję srand(), która służy do zainicjowania tzw. ziarna, czyli początkowej wartości losującej
3. Funkcję srand() należy wywołać podając jako jej argument funkcję time(NULL), która zwraza liczbę sekund, jako upłynęła od początku ery Unixa (dzięki czemu z każdym uruchomieniem uzyskujemy inną sekwencję liczb pseudolosowych)

***Przykład 1:***

```text
Program, który losuje jedną liczbę całkowitą i wypisuje ją na ekran.  
 #include<iostream>  
 #include<ctime>  
 #include<cstdlib>  
 using namespace std;
```

```text
int main()  
 {  
    int x;  
    srand(time(NULL));  
    x=rand();  
    cout<<x;  
 }
```

Aby wygenerować liczbę z zakresu:

Naturalną &lt;0, a&gt;

**x=rand()%(a+1)**

Całkowitą &lt;a,b&gt;

**x=a+rand()%(b-a+1)**

Rzeczywistą &lt;a,b&gt;

**x=a+((float)rand()/(RAND\_MAX))\*(b-a)**

***Przykład 2***:

Program, który losuje jedną liczbę całkowitą z przedziału od 0 do 5 i wypisuje ją na ekran.

```text
int main()  
 {  
    int x;  
    srand(time(NULL));  
    x=rand()%6;  
    cout<<x;  
 }
```
