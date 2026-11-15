# Instrukcja break, continue

Instrukcja **break**

`Słowo kluczowe break` wprowadzone do pętli powoduje automatyczne wyjście z pętli i przejście do instrukcji znajdujących się poza pętla w programie (pomimo faktu, że warunek działania pętli jest jeszcze prawdziwy)

**Przykład 1:**

```cpp
a=10
while(a<100){
   if(a==80)
      break;
   a+=10
}
cout<<"Jestem poza petla, a="<<a;
```

Zauważ, że program wyświetli wartość a=80, ponieważ instrukcja break przerwie natychmiast działanie pętli, pomimo faktu, ze dla a=80 &lt;100. Nie wykona się też instrukcja dodawania znajdująca się za `break`.

---

Instrukcja **continue**

`Continue` przerywa działanie <u>tylko bieżącego</u> obiegu pętli, tzn. po słowie kluczowym `continue` nie wykona się już żadna następna instrukcja wewnątrz pętli. Jednak w odróżnienie do `break`  program wraca ponownie do sprawdzania warunku działania pętli i jeśli jest spełniony to znowu wykonują się jej instrukcje.

**Przykład 2:**  
Program wczytuje 5 liczb parzystych i oblicza ich sumę - użytkownik wpisujący liczby z klawiatury nie musi kontrolować faktu, czy wpisuje liczby parzyste czy nie.

```cpp
i=0
suma=0
while(i<10){
  cin>>a;
  if (a%2==1)
     continue;
  i+=1;
  suma+=a;
}
```

Jeśli użytkownik wpisze liczbę nieparzystą, to program wychodzi z pętli - nie wykona się sumowanie tej liczby oraz nie wykona się również zliczenie tej liczby do ilości wczytanych. Program powraca do warunku pętli i jeśli nie wczyta 5 liczb parzystych, kontynuuje działanie.

---

**Przykład1**  
Wczytaj 10 liczb i dodaj do siebie tylko nieparzyste  
`for(i=0;i<10;i++)`  
`{`  
 `cin >> a;`  
 `if(a%2==0)continue;`  
 `suma=suma+a;`  
`}`

**Przykład2**  
Przeanalizuj poniższy kod i podaj liczbę # i \*

```cpp
for(i=0;i<5;i++){
     cout << "#";
     if(i%2==0)continue;
     cout << "*";
}
```

*ile #:5*  
*ile \*:2*

**Przykład3**  
Wczytuj liczby dopóki nie wczytasz zera, ale nie więcej niż 10 liczb  
`for(i=0;i<10;i++)`  
`{`  
 `cin >> a;`  
 `if(a==0)break;`  
`}`

**Przykład4**  
Przeanalizuj poniższy kod i podaj liczbę # i \*  
  
for(i=0;i&lt;5;i++){

```cpp
     cout << "#";
     if(i%2==0)break;
     cout << "*";
}
```

*ile #:1*  
*ile \*:0*
