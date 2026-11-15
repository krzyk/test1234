# Wyszukiwanie binarne

## Wyszukiwanie połówkowe (binarne)

Dla uporządkowanej (posortowanej) tablicy do sprawdzenia, czy znajduje się w niej element np możemy zamiast wyszukiwania liniowego (złożoność liniowa) zastosować wyszukiwanie binarne (złożoność logarytmiczna). Metodę oprogramowujemy podobnie do omawianej bisekcji.

Wyszukiwanie binarne:

- korzysta z metody dziel i zwyciężaj
- w każdym obiegu pętli algorytm redukuje liczbę elementów o połowę, zatem klasa złożoności obliczeniowej jest równa O(log *n*). Jest to bardzo korzystna złożoność. Na przykład w algorytmie wyszukiwania liniowego przy 1000000 elementów należało wykonać aż 1000000 porównań, aby stwierdzić, iż elementu poszukiwanego nie ma w zbiorze. W wyszukiwaniu binarnym wystarczy 20 porównań.

Omówienie metody na przykładzie: (l-lewa strona, p-prawa strona)

Niech będzie dana tablica 5-elementowa, *a = {1, 2, 4, 6, 7}*.  
Poszukajmy w niej element *x = 2*.  
Na początku *l = 1*, *p = 5*.  
Wybieramy element środkowy *s = (1 + 5) / 2 = 3*.  
Sprawdzamy czy *a[3]* jest równe 2? Nie, element ten jest równy 4, jest on większy od 2 zatem modyfikujemy *p = s - 1 = 3 - 1 = 2*.  
Wybieramy element środkowy *s = (1 + 2) / 2 = 1*.  
Sprawdzamy czy *a[1]* jest równe 2? Nie, element ten jest równy 1, jest on mniejszy od 2 zatem modyfikujemy *l = s + 1 = 1 + 1 = 2*.  
Wybieramy element środkowy *s = (2 + 2) / 2 = 2*.  
Sprawdzamy czy *a[2]* jest równe 2? Tak, znaleźliśmy szukany element pod indeksem 2.  
  
Poszukajmy teraz element *x = 5*.  
Na początku *l = 1*, *p = 5*.  
Wybieramy element środkowy *s = (1 + 5) / 2 = 3*.  
Sprawdzamy czy *a[3]* jest równe 5? Nie, element ten jest równy 4, jest on mniejszy od 5 zatem modyfikujemy *l = s + 1 = 3 + 1 = 4*.  
Wybieramy element środkowy *s = (4 + 5) / 2 = 4*.  
Sprawdzamy czy *a[4]* jest równe 5? Nie, element ten jest równy 6, jest on większy od 5 zatem modyfikujemy *p = s - 1 = 3*.  
W tym momencie *l* jest większe od *p*, zatem kończymy wyszukiwanie. Elementu o wartości 5 nie ma w przeszukiwanej tablicy.

**Polecenie:**Napisz program dla tablicy wypełnionej 100 el kolejnych liczb parzystych.
