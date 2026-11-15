# Funkcje - teoria

Zalety dzielenia programu na podprogramy:

- dany podprogram można wywołać kilka razy - zatem zmniejszamy liczbę linijek kodu
- program łatwiej zrozumieć

**Programowanie proceduralne** - dzielenie kodu na podprogramy.

Zaleca się budowanie podprogramów na **zmiennych lokalnych** - tzn każda zmienna   
użyta w podprogramie jest w nim zadeklarowana

## Funkcja nie zwracająca wartości:

`void cos(int ile) //nagłówek funkcji`, **zmienna 'ile' to parametr formalny**   
`{`

```cpp
      for(i=0;i<ile;i++) cout<<"*";
}
int main()
{
......
cos(5); //wywołanie funcji
int a=3;
cos(a); // zmienna a to parametr aktualny
...
```

`}`  
void - typ funkcji - oznacza, że funkcja nic nie zwraca

## Funkcja zwracająca wartość:

```cpp
int mnoz(int x) //nagłówek funkcji
{
    return x*2; //zwracana wartość
}
int main()
{
......
int w; //wywołanie funcji
w=mnoz(5);
....
}
```

W tych funkcjach parametry **przekazywane są przez wartość**, funkcja działa na **kopiach zmiennych**.

By wymusić na funkcji **nie tworzenie kopii** musimy przekazać parametry **przez referencje**

### Przekazanie parametrów przez referencje:

```cpp
void zeruj(int &a)
{
a = 0;
}
int main()
```

{  
`...`  
`int a=5;`  
`zeruj(a);`

```cpp
...
}
UWAGA - funkcji przekazujacych parametry przez referencje nie mozna wywolywac dla wartosci czyli nie mozna zeruj(5) 

W JEDNYM PROGRAMIE MOZNA TWORZYC FUNKCJE O TYCH SAMYCH NAZWACH JEDYNIE WTEDY, GDY MAJA ONE INNA LISTE PARAMETROW, np int pole(int x,int y) oraz int pole(int x) JEST TO TAK ZWANE PRZECIAZENIE NAZWY FUNKCJI
```

## Funkcje i tablice

w budowie
