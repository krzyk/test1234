# Teoria funkcje 2 - przeładowanie, funkcje inline

**Overloading**

**Przeładowanie funkcji** (overloading) to mechanizm, który pozwala tworzyć wiele funkcji o tej samej nazwie, ale różniących się liczbą lub typami argumentów.

```cpp
int dodaj (int a, int b){....}
int dodaj (int a, int b, int c){...}
int dodaj (int a, double b){....}
```

double dodaj (int a, int b) {...} //BŁĄD! Nie można przeładować funkcji tylko na podstawie typu zwracanego!

UWAGA!   
Funkcje o tej samej nazwie aby mechanizm przeładowania działał prawidłowo muszą różnić się: **1)liczbą argumentów** albo **2) typem argumentów** albo **3) kolejnością argumentów**

---

**Funkcje inline**

Funkcje w języku C++ możemy opatrzeć przedrostkiem inline. Funkcje tego typu kompilator może (ale nie musi) umieszczać w linii kodu bezpośrednio w miejscu ich wywołania. Nie ma wówczas całego mechanizmu wchodzenia i wychodzenia z funkcji, co zwiększa wydajność (szybkość) całego procesu.

```cpp
inline kwadrat(int x){
       return x*x;
}
```

Jeśli kompilator uzna stosowanie funkcji w linii, to wówczas będzie podmieniał wywołanie:

`y=kwadrat(a);` na:  `y=a*a;`  czyli tak, jakby było w linii.

Kiedy stosować funkcje typu **inline**?  
Tylko dla krótkich funkcji, które często będą wywołane w programie (bez użycia pętli). Funkcje inline muszą być w całości definiowane na samej górze tekstu programu (nie dopuszcza się tworzenia wstępnej deklaracji, a następnie definicji funkcji.
