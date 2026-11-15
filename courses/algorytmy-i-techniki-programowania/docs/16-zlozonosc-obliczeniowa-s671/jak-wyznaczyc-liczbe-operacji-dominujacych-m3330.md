# Jak wyznaczyć liczbę operacji dominujących

*Uwaga: LOP- liczba operacji dominujących, Z - złożoność*

**Przykład 1: algorytm liniowy**

int r = 5;  
pole = r\*r\*3.14; // ponieważ to alg. liniowy, liczymy liczbę operacji arytmetycznych -&gt; LOP=2, Z=O(1)

**Przykład 2: algorytm warunkowy**

int r = 5;  
if(r&gt;0)  // ponieważ to alg. warunkowy, liczy liczbę zapytań(warunków) -&gt; LOP=1, Z=O(1) czyli stała  
   cout&lt;&lt;"mozna wyznaczyć pole";  
pole = r\*r\*3.14;

**Przykład 3: algorytm iteracyjny - suma elementów tablicy**  
int tab[n];  
for(int i=0;i&lt;n;i++) //zapytań "czy i&lt;n" wykona się n razy (dokładniej n+1, ale tą 1 zwykle się pomija) --&gt;LOP=n, Z=O(n) czyli liniowa  
    suma+=tab[i];

**Przykład 4: algorytm iteracyjny - suma elementów tablicy na indeksach parzystych**  
int tab[n];  
for(int i=0;i&lt;n;i++) //zapytań "czy i&lt;n" wykona się n razy --&gt;LOP=n  
  if (i%2==0). //zapytań  wykona się n razy --&gt;LOP=n  
    suma+=tab[i];

Finalnie mamy n+n, czyli LOP=2n, ale Z=O(n) czyli liniowa (wkład "2" się pomija w oznaczaniu złożoności, jako mniej znaczący)

**Przykład 5: algorytm iteracyjny - wypisywanie liczb trzycyfrowych**  
int tab[n];  
for(int i=1;i&lt;n;i++){ //zapytań n-1  
  for(int j=0;i&lt;n;i++) //zapytań \*n  
    for(int j=0;i&lt;n;i++) ////zapytań \*n  
           cout&lt;&lt;i&lt;&lt;j&lt;&lt;k;  
  cout&lt;&lt;endl;}

Finalnie mamy (n-1)\*n\*n, czyli LOP=n^3-n^2, ale Z=O(n^3) czyli złożoność wielomianowa (wkład "n^2" się pomija w oznaczaniu złożoności, jako mniej znaczący)
