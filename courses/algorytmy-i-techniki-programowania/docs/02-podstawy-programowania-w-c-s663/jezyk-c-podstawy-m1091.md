# Język C++ - podstawy

*Język C++ powstał w latach 80 XXw.  początkowo jako rozszerzenie języka C o obiektowość. Najnowsza wersja języka to C++26, ale nie jest obsługiwana jeszcze przez wszystkie kompilatory.   
**Dokumentacja języka:******<https://en.cppreference.com/w/>***

## Podstawowe pojęcia

Język C++ jest językiem **wysokiego poziomu**. Oznacza to, że nie jest rozumiany przez maszynę bezpośrednio.

**Implementacja** - tworzenie kodu, pisanie programu

**Kod maszynowy** - rozumiany przez maszynę, ciąg 0 i 1.

**Kompilacja** - tłumaczenie kodu wysokiego poziomu na kod maszynowy.

**Kompilator -**program tłumaczący kod wysokiego poziomu na kod maszynowy.

Programiści podczas implementacji popełniają błędy:

- **błędy kompilacji -** np brak średnika, literówka, wykrywane przez kompilator.
- **błędy logiczne (wykonania)** - błędy merytoryczne np złe policzenie pola figury

Do znalezienia błędów wykonania przydatny jest **debbuger.**

**Etapy powstawania programu:**

1. implementacja - tworzenie kodu źródłowego
2. kompilacja
3. linkowanie (konsolidacja) - dołączanie skompilowanych bibliotek
4. kod wynikowy

---

## **"Ramy programu"**

```cpp
#include <iostream>
using namespace std;

int main()
{
      cout << "witaj swiecie";
      //...

      return 0;
}
```

---

## **Komentarze:**

- //
- /\* \*/ (komentarz blokowy)

---

## **Zmienne**

**Zmienna** - obszar w pamięci komputera, której możemy przypisywać różne wartości.

**Deklaracja zmiennej** - rezerwacja pamięci dla zmiennej w pamięci komputera.  
`int a; //deklaracja`  
`int b=7; //inicjalizacja`

Kompilator nie zeruje zadeklarowanych zmiennych. Powyżej zadeklarowania zmienna `a` otrzyma przypadkową wartość.

**Deklaracja stałej (stałe nazwane)** - wyrażenia, mające ustaloną wartość, która nie zmiania się w trakcie działania programu. Stałą może być liczba, lub całe wyrażane, np. 1+2  
`const float EULER = 2.71`  
lub przy użyciu dyrektywy preprocesora:  
`#define EULER 2.71`

**Nazwy zmiennych** nie mogą zawierać polskich znaków. Dozwolone znaki to: (a..z), (A...Z), podkreślenie ( \_ ) i cyfry (0...9). Nazwa zmiennej **nie może się również zaczynać od liczby**. Zmienne muszą posiadać unikatową nazwę w obrębie całego programu (dokładniej to w obrębie funkcji, ale o tym przypomnę gdy dojdziemy do tematu funkcji). Warto tu również podkreślić, że zmienna **int abc;** nie jest tą samą zmienną co **int ABC;**. Są to dwie różne zmienne, o różnych nazwach.

---

## Typy danych <https://en.cppreference.com/w/cpp/language/types>

| Nazwa typu | Ilość Bajtów | Zakres wartości |
| --- | --- | --- |
| bool | 1 | **false** lub **true** |
| char | 1 | od -128 do 127 |
| unsigned char | 1 | od 0 do 255 |
| wchar\_t | 2 | od 0 do 65'535 |
| short | 2 | od -32'768 do 32'767 |
| unsigned short | 2 | od 0 do 65'535 |
| int | 4 | od -2'147'483'648 do 2'147'483'647 |
| unsigned int | 4 | od 0 do 4'294'967'295 |
| long | 4 | od -2'147'483'648 do 2'147'483'647 |
| unsigned long | 4 | od 0 do 4'294'967'295 |
| long long | 8 | od -9'223'372'036'854'775'808 do 9'223'372'036'854'775'807 |
| unsigned long long | 8 | od 0 do 18'446'744'073'709'551'615 |
| float | 4 | 3.4E +/- 38 (7 cyfr) |
| double | 8 | 1.7E +/- 308 (15 cyfr) |
| long double | 8 | 1.7E +/- 308 (15 cyfr) |

Powyższe rozmiary danych są podane dla 32-bitowego kompilatora Visual C++. Jeśli chcesz sprawdzić ile w rzeczywistości zajmuje określony typ danych dla Twojego kompilatora, wystarczy napisać prosty program i wykorzystać w nim słowo kluczowe **sizeof**.

```cpp
cout << "rozmiar zmiennej typu int to  " << sizeof( int ) << "bajtów"<< endl;
```

### Słowo kluczowe unsigned

Wyraz "unsign" ten możemy wpisywać przed każdą zmienną całkowitą/znakową, jeśli chcemy, aby przechowywane w zmiennej wartości były nieujemne. Dzięki temu do zmiennej możemy zapisać dwa razy większą liczbę dodatnią. Nie możemy natomiast zapisać już do niej liczby ujemnej.

### Konwersja typu

- **niejawna (automatyczna)**, np.   
  `float x = 1;` //kompilator sam, automatycznie zamienia liczbę na float (1.0) z int (1)
- **jawna**  
  `float x = 5.1;`  
  `int y = (int)x;`     
  lub:  
  int y = int(x);  
    
  W języku C++ można również dokonywać konwersji przy użyciu operatora `static_cast,` np:  
  `float pi = 3.14;`  
  `int pi_nowe = static_cast<int> (pi);`

---

## Operatory

- arytmetyczne: +,-,\*,/ (zwraca wynik dzielenia całkowitego lub rzeczywistego),% (zwraca resztę z dzielenia)
- przypisania =, +=,-=,/=, \*=
- relacyjne: &gt;,&lt;,&gt;=,&lt;=,!=,==
- logiczne: && (and), ||(or), ! (do budowania warunków złożonych)
- [bitowe (&, I, ^, ~, &lt;&lt;, &gt;&gt;)](https://www.algorytm.edu.pl/wstp-do-c/operatory-w-c#priorytety)

### Priorytety operatorów

1. Nawiasy
2. Operatory inkrementacji i dekrementacji (w wersji pre, czyli ++i, --i)
3. Operator rzutowania (np. (int)x)
4. Operatory mnożenia, dzielenia, modulo
5. Operatory dodawania, odejmowania
6. Operatory przesunięcia bitowego &lt;&lt;, &gt;&gt;
7. Operatory relacyjne - porównywania (==, !=, &gt;, &lt;, &gt;=, &lt;=)
8. Operatory bitowe (^, &, I, ...)
9. Operatory logiczne (&&, II, ...)
10. Operator warunkowy ?:
11. Operatory przypisania (=, +=, \*=, itd.)  
      
    Przykłady:

- Operatory logiczne mają niższy priorytet niż operatory relacyjne, dlatego w wyrażeniach takich jak poniższe nie musimy stosować nawiasów:  
  if(x&lt;6 && y&gt;=6)
- Operatory mnożenia, dzielenia i module mają niższy priorytet niż operacje inkrementacji, dlatego też:  
  int a =15, b=5;  
  int d = ++a + a%c;    // d= 16+16%5=17

### Operator / i konwersja typów:

Operator / pełni funkcję operatora dzielenia całkowitego i rzeczywistego, np.

int a,b,c;  
float x,y,z;  
a = b/c; // dzielenie całkowite, bo b i c to liczby całkowite  
x = b/c; // dzielenie całkowite mimo, że x jest typu float, ważne że b i c to liczby całkowite  
x = y/z; // dzielenie rzeczywiste, bo y i z to liczby rzeczywiste  
x = y/a; // dzielenie rzeczywiste, bo y jest rzeczywiste i narzuca typ

**Jak zatem podzielić dwie liczby całkowite, by dostać wynik rzeczywisty:**  
sposób 1 awans x = 1.0\*a/c;  
sposób 2 jawna konwersja typu, rzutowanie typu x = (float)a/c;

### Rożne sposoby zapisu działań:

- instrukcję a = a+ 5; można zapisać: a+=5
- instrukcję a = a / 5; można zapisać: a/=5
- itd dla innych działań
- instrukcję a = a\*(x+5); można zapisać: a \*= (x+5); nawias jest konieczny

### Inkrementacja/dekrementacja

Inkrementacja - instrukcja zwiększenia wartości zmiennej o 1. Można zapisać to na kilka sposobów:

- a = a+1
- a+=1
- a++ (postinkrementacja)
- ++a (preinkrementacja)

Dekrementacja - instrukcja zmniejszenia wartości zmiennej o 1. Można zapisać to na kilka sposobów:

- a = a-1
- a-=1
- a-- (postdekrementacja)
- --a (predekrementacja)

a++ oraz ++a - różnica:  
a=3;  
b=a++; // b przyjmie wartość 3, natomiast potem zmienna a zwiększy się na 4;  
a=3;  
b=++a; // b przyjmie wartość 4, bo zwiększenie będzie najpierw
