# Pętla for - teoria podstawowa

# Pętla for

## Składnia:

`for (i`nicjalizacja\_zmiennej\_sterującej\_pętlą  **;**  warunek\_działania\_pętli **;** instrukcja\_skoku)   
      instrukcja\_wykonywana\_w\_pętli;

**Wszystkie pętle w C/C++ działają dopóki warunek jest prawdziwy.**

---

**Przykład1:**

```cpp
int i;
for (i=1;i<5;i++) 
    instrukcja;
```

lub:

```cpp
for (int i=1;i<5;i++) //tutaj zmienna  sterująca i zadeklarowana jest tylko wewnątrz pętli i poza pętla nie jest znana
```

jeśli wykonujemy więcej niż jedną instrukcję w pętli używamy nawiasów {}:

```cpp
for (int i=1;i<5;i++){                    {
    instrukcja1;
    instrukcja2;
}
```

**Przykład2:**  
Warunek występujący w pętli nie musi być nałożony na zmienną sterującą:

```cpp
int suma = 0; int a; 
for(int i=1; suma < 100; i++)
{
   cout<<"podaj liczbę";
   cin>>a;
   suma = suma+a;
}
```

**Przykład3:**  
Czy potrzebna jest zmienna i? Mogłoby tu jej nie być. Poprawny jest również taki zapis pętli:  
`for(;suma<100;) //UWAGA, średniki są konieczne!!!`

Ale wówczas czytelniejsze jest zastąpienie jej pętlą while (`while(suma<100)`)

******Różne inne wydania pętli for:******

1. `for(;;);` // pętla nieskończona
2. `for (i=1;i<10;)`
3. `i=1;`  
   `for(;i<10;)i++;`
4. `for (char i=’a’;i<’z’;i++)`  .... ; //zmienna sterująca pętlą może być typu znakowego, bo jest to typ porządkowy
5. `for(i=1, k=1; i<5; i++, k++)` //w pętli możemy inicjować więcej niż jedną zmienną - wówczas oddzielamy je przecinkiem; również więcej niż jedną instrukcję skoku
6. **Instrukcja skoku to nie koniecznie i++ lub i--**

   ```cpp
   for(i=0;i<100;i+=5) 
   to to samo co for(i=0;i<100;i=i+5)
   ```

---

## Przeanalizuj fragment kodu:

```cpp
for (i=1;i<5;i++) 
     instrukcja;
cout<<i;
```

Ile razy wykona się pętla?    *odpowiedź: 4 razy*  
Jaka będzie wartość zmiennej i po zakończeniu pętli? *odpowiedź: i=5*
