# Lista zadań vector/set

1. Skopiuj poniższy wektor do swojego kodu:  

   vector&lt;int&gt; x = { 2,7,1,1,4,9,3,2,1,4,1,9,6,1,3,0,1,2,3,6,8,5,6,9,  
    3,0,8,1,8,8,7,0,7,8,5,0,2,2,3,7,1,7,2,4,7,7,5,9,0,7,7,9,2,2,2,7,  
    0,0,5,4,6,3,9,3,5,1,0,0,9,2,9,2,8,5,0,8,5,7,0,9,6,4,9,7,8,8,6,5,  
    4,3,2,5,8,9,4,6,8,7,9,9 };  
     
   Następnie wyświetl kolejne liczby określające odległość między kolejnymi wartościami 9 w wektorze. Przyjmij, że sąsiadujące bezpośrednio dziewiąte dzieli odległość 0, dziewiątki rozdzielone jedną liczbą (np. 9,4,9) dzieli odległość 1, itd.
2. Utwórz wektor/listę zawierającą następujące cyfry:  
     
   vector&lt;int&gt; v = {1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9 };  
     
   1. znajdź w wektorze i wyświetl wszystkie podciągi trójelementowe (trzy kolejne liczby wektora), które tworzą ciągi niemalejące
   2. znajdź jeden najdłuższy podciąg niemalejący: ile ma elementów?
   3. policz liczbę wystąpień każdej liczby w wektorze
3. Utwórz trzy wektory z następującą zawartością:  
     
   v1={1,3,5,7,9}, v2={1,4,7,11,15}, v3={1,2,3,4,5,6,7,8,9,20}  
     
   Potraktuj je jak zbiory, w których każdy elementy może wystąpić tylko jeden raz. Przykładowo, gdybyśmy chcieli dodać liczbę 5 do zbioru v1, to zbiór v1 nie uległby zmianie bo 5 już tam jest. Dla podanych wektorów/zbiorów wyświetl:
   1. część wspólną zbiorów v1 i v2
   2. różnicę zbioru v3 i sumy zbiorów v1+v2 to znaczy: v3-(v1+v2) = ?
   3. sumę wszystkich zbiorów v1+v2+v3
4. Utwórz funkcję, która w wektorze przekazanym jako argument szuka wszystkich podciągów przynajmniej dwuelementowych złożonych z takich samych liczb. Funkcja powinna wyświetlać wszystkie takie podciągi, **od najkrótszych po najdłuższe** podając indeks pierwszego i ostatniego elementu dla każdego podciągu, np.: dla {2, 1, 1, 3, 5, 3, 3, 3, 4, 8, 8}  
     
   - 1,1 na pozycjach od 1 do 2
   - 3,3 na pozycjach od 5 do 6
   - 8,8 na pozycjach od 9, 10
   - 3,3,3 na pozycjach od 5 do 7
