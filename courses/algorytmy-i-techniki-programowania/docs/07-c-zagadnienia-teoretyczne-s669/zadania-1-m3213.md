# Zadania 1

1. Zdefiniuj stałą g - (g=9,81 przyspieszenie ziemskie) wykorzystując #define.
Policz, z jaką prędkością spada piłka, która uderza w ziemię po czasie 5s? (v=g\*t)

1. umieść definicje funkcji po funkcji main()
2. dodaj deklaracje funkcji przed funkcją main()
3. którą z instrukcji w Twoim programie zajmie się preprocesor?

2. Napisz funkcję ulamek( float licznik, float mianownik), która zwróci wartość licznik/mianownik. A następnie:
   1. zdefiniuj stałą przechowywającą prędkość światła (w km/s) - użyj #define
   2. zdefiniuj odległość Ziemia-Słońce w km - użyj const
   3. wyznacz po jakim czasie dowiemy się, że Słonce zgaśnie (wykorzystaj wzór v=s/t) - wykorzystaj funkcję ułamek()
   4. stwórz zewnętrzny plik o nazwie funkcje.cpp i umieść w nim są definicję funkcji ułamek
   5. usuń definicję funkcji ułamek z pliku głównego i dołącz odniesienie do pliku funkcje.cpp (#include "funkcje.cpp")
   6. wskaż, co zrobi w tym programie preprocesor, a co linker
   7. dokonaj kolejnej modyfikacji:
      1. usuń deklaracje funkcji z pliku
      2. stwórz plik nagłówkowy funkcje.h i wklej tam deklaracje funkcji
      3. dołącz plik nagłówkowy w programie głównym
3. Napisz program, który sprawdzi, jak płynie czas dla astronauty poruszającego się z prędkościami bliskimi prędkości światła:
   1. zdefiniuj stałą c
   2. wczytaj prędkość rakiety v\_Astronauty (np. 200 000 km/s) oraz czas, jaki upłynął na Ziemi t\_naZiemi (np. 10 lat)
   3. sprawdź, czy po podniesieniu v do kwadratu wartość zmieści się w typie int
   4. wykorzystując wzór: t\_DlaAstronauty=t\_NaZiemi\*sqrt(1-(v\_Astronauty/c)^2)m policz ile czasu upłynęło dla astrounaty (t\_DlaAstronauty)
