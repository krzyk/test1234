# Lista 4 - anagramy

1. Wczytaj/wpisz/wylosuj liczby całkowite z przedziału od 0 do 5 do tablicy 20 elem, a następnie policz ile w niej jest 0,1,2,3,4,5. Wykorzystaj tablicę zliczającą. Tablica zliczająca najpierw wypełniona jest zerami, a następnie a następnie jej wartości zostaną odpowiednio zwiększane o 1 np
   - tablica pierwsza: 1,1,1,0,1,2,1,0,0,3,5,3,1,1,0
   - tablica zliczająca na początku: 0,0,0,0,0,0
   - tablica zliczająca po zrealizowaniu zadania: 4,7,1,2,0,1
   - bo mamy 4-zera,7-jedynek,1-dwojke,2-trojki,0-czworek,1-piatkę
2. Wczytaj dwa słowa i sprawdź, czy są **anagramami** (są zbudowane z tych samych liter) np słowa "rower" i "rrowe" są anagramami. WSKAZÓWKA: liczbę występowania danej litery w słowie rejestruj w tablicy zliczającej.
3. **FRAGMENT ZADANIA MATURALNEGO:**Liczba naturalna *a* jest **anagramem znakowym** liczby naturalnej *b*, jeśli można ją zapisać za pomocą cyfr występujących w zapisie liczby *b*, używając każdej cyfry dokładnie tyle razy, ile razy występuje w zapisie liczby *b*.  Np. liczba 12121 jest anagramem **znakowym** liczby 11212. Napisz i wywołaj funkcję, która sprawdza, czy dwie liczby wczytane z klawiatury są swoimi anagramami **znakowymi** i wypisuje słowo *tak* albo *nie*, w zależności od wyniku sprawdzenia.
