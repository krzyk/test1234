# Schemat Hornera

# Schemat Hornera

Algorytm znajduje wartość wielomianu dla podanego x.

Przeanalizujmy wielomian, stopnia 3:

W(x)=3x<sup>3</sup>+2x<sup>2</sup>-5x+2

Przy "naiwnym" podejściu program wykonuje bardzo dużo mnożeń:

W(x)=3\*x\*x\*x+2\*x\*x-5\*x+2

Sytuacja zmienia się jeżeli "przekształcimy wielomian":

W(x)=x\*(3\*x\*x+2\*x-5)+2 = x\*(x\*(3\*x+2)-5)+2

Nowa postać wielomianu ma w sobie znacznie mniej mnożeń.

Liczba mnożeń dla wielomianu stopnia n:

- algorytm naiwny: n+(n-1)+(n-2)+ ....+2+1 mnożeń
- schemat Hornera: n mnożeń

Do napisania programu należy wykorzystać odpowiednią strukturę danych do przechowania wielomianu - tablicę, najlepiej dynamiczną jeśli nie znamy stopnia wielomianu.

Dla wielomianu W(x)=3x<sup>3</sup>+2x<sup>2</sup>-5x+2 powstanie tablica {3,2,-5,2}

POLECENIA:

1. Następujący wielomian W(x)=4x<sup>4</sup>-3x<sup>2</sup>+x-6:
   - przedstaw w postaci schematu Hornera
   - znajdź wartość wielomianu dla x=2 dla postaci Hornera oraz dla postaci "klasycznej"
   - podaj tablicę potrzebną do napisania programu. Uwaga: W wielomianie mamy współczynniki o wartości zero.
2. Napisz funkcję horner, która dla podanego x znajdzie jego wartość, przy czym:
   - funkcja jako parametr przyjmuje stopień wielomianu, tablice współczynników oraz x dla którego chcesz znaleźć wartość
   - funkcja zwraca wartość typu float
   - wywołaj funkcję dla wielomianu z zadania 1 oraz dla dowolnego wczytanego wielomianu
3. Podaj liczbę mnożeń w algorytmie naiwnym: skorzystaj z sumy ciągu arytmetycznego.
4. Podaj rekurencyjną postać alg Hornera.
