# C++11/niestandardowe kontrukcje

## Inicjalizacja zmiennych (od C++11)

Inicjalizacja zmiennych to nadanie zmiennym jej wartości początkowej. Można ją wykonać na kilka sposobów:

1. *Inicjalizacja C-podobna:*  
   `int x = 1;`
2. *Inicjalizacja bezpośrednia (konstruktorowa)*  
   `int x(1);`
3. *Inicjalizacja jednolita bezpośrednia*  
   `int x{1};`  
   `int x{}; //w tym przypadku zostanie nadana wartość 0, jest to tzw. inicjalizacja zerowa`
4. *Inicjalizacja jednolita kopiująca  
   `int x={1};`*

## Deklaracja zmiennej z dedukcją typu (od C++11)

Kompilator może sam ustalić, jakiego typu powinna być dana zmienna. Może to zrobić na dwa sposoby:

1. Przy użyciu specyfikatora decltype  
   `int x = 5;`  
   `decltype (x+100) y;`
2. Przy użyciu słowa kluczowego auto  
   `int x = 5;`  
   `auto y = x+1;`  
   lub  `auto y(x+1)`;  lub `auto y{x+1}`

## Własne nazwy dla typów podstawowych

W języku C++ możemy stworzyć aliasy nazw dla rozbudowanych typów danych na dwa sposoby:

1. Przy użyciu specyfikatora typedef:  
     
   **typedef** typ\_istniejący alias;  
     
   `typedef unsigned long long ull;`
2. Przy użyciu słowa kluczowego using  
     
   **using** alias = typ\_istniejący;  
     
   `using ull = unsingned long long;`

 W obu przypadkach, po zastosowaniu sposobu 1 lub 2 pod nazwą ull będzie dostępny typ unsigned long long, dlatego też będzie można tak zadeklarować ten typ danych:

```cpp
ull x;     //x będzie typu unsingned long long
```
