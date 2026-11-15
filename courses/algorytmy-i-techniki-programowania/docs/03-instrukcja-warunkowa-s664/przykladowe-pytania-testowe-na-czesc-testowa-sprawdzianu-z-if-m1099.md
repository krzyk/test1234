# Przykładowe pytania testowe na część testową sprawdzianu z if

1. Instrukcja inkrementacji wykona się w poniższym kodzie ………….. razy.

```cpp
int liczba=0, i=0;
i=i+1;
if(liczba<0) liczba++;
```

2. Co oznacza wpis w kodzie programu

```cpp
    #include<cmath>
```

3.W każdym podpunkcie przyjmij, że i=3.

```cpp
a) c=5%i;   c = ………………..
b) i+=4;     i = ………………..
c) i--;     i = ………………..
```

W podpunkcie tym zmniejszyliśmy wartość zmiennej i o jeden, co w programowaniu nazywa się ……………………………..

d) Dokończ fragment programu tak, by zmienna c przechowywała wynik rzeczywistego dzielenia liczby 5 przez i:

```cpp
float c = ……………………………………………………
```

4. Wyrażenie x \*= y + 1 w języku C++ jest równoważne następującej instrukcji:

```cpp
a. x = (x * y)++
b. x = ++(x * y)
c. x = x * (y+1)
```

5. Co zostan ie wypisane na ekranie dla x=0?

```cpp
if(x<5 && x>0) cout<<“*”;
else
    if(x<0) cout<<“**”;
    else cout<<“***”;
```

1. `*`
2. `**`
3. `***`
4. `Nic`

6. Co wyświetli poniższy fragment programu napisany w C++?

```cpp
cout<< 2/3;
```

7. Co wyświetli poniższy fragment programu napisany w C++?

```cpp
cout<< 5 % 2;
```

8. Jaką wartość będą miały zmienne po wykonaniu kodu:

```cpp
i=10;
j=i++;
j*=2;
k=++i+j;
```

i=……………… j=………………… k=……………………

9. Program przechodzi kompilację, ale niestety nie działa poprawnie – wypisuje złe dane dla wprowadzonych liczb. Oznacza to, że programista popełnił:

1. Błąd logiczny
2. Błąd wykonania
3. Błąd kompilacji

10. jaka jest wartość logiczna wyrażenia

```cpp
7>1 && 0                ............................................
2<10 && 2>20            ............................................

„Ala ma kota” && 1<2    ............................................

!1 || 1<5  ............................................
```

`11.` Jaka wartość mają zmienne x i y po wykonaniu poniższych instrukcji? (zapisz obliczenia)

x = 5;

y = x - (x % 3) \* 3;

y\*=x+2;
