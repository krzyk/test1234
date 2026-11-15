# Lista 3 - palindromy, palindromy na kodach ASCII, cyfrowe

1. Stwórz nowe słowo, które będzie odwrotnością słowa wczytanego (zadanie (odnośnik niedostępny w kopii kursu) wykonaj na dwa sposoby: 1) przy uzyciu pętli 2) przy użyciu funkcji reverse()
2. Wczytaj słowo i sprawdź, czy jest **palindromem**
3. Palindromem cyfrowym nazywamy taką liczbę, która czytana od prawej i lewej daje taką samą liczbę, np: 12321, 121, 1441. Napisz program, który wczyta z klawiatury liczbę, a następnie sprawdzi, czy jest palindromem cyfrowym:
   1. do rozwiązania zadania użyj funkcji to\_string() która zamieni wczytaną liczbę na stringa
   2. nie używaj wbudowanych funkcji, ale użyj odpowiednio operacji dzielenia całkowitego oraz % do wyłuskania kolejnych cyfr z liczby:
      1. na początku możesz założyć że sprawdzasz tyko liczby 3 cyfrowe
      2. rozwiń zadanie i wykonaj dla liczb o różnej liczbie cyfr
4. Palindromem cyfrowym na kodach ASCII nazywamy takie słowo, w którym każda kolejna para skrajnych znaków ma w sumie taką samą wartość, obliczając ją na podstawie kodów  ASCII. Gdy słowo ma nieparzystą liczbę znaków, to nie bierzemy pod uwagę środkowego znaku.

   Na przykład takim palindromem jest słowo ABYZ, gdyż litery A, B, Y, Z mają kody  ASCII odpowiednio: 65, 66, 89 i 90. Zatem dla A i Z mamy 65+90=155, a dla B i Y mamy 66+89=155.

   Wszystkie słowa w plikach do zadania (odnośnik niedostępny w kopii kursu) są zbudowane z wielkich  liter alfabetu angielskiego  i każde ze słów ma długość od 3 do 30 liter.

   1. sprawdź czy słowo MEGEGIA  jest palindromem cyfrowym
   2. napisz i wywołaj funkcję czy\_palindrom\_ascii() sprawdzającą, czy wczytane słowo jest palindromem na kodach ASCII
   3. sprawdź dla wczytanego słowa, czy można wymienić jeden znak na inny w danym słowie tak, aby uzyskać palindrom na kodach ASCII
   4. odczytaj słowa z pliku tekstowego, przepisz do pliku p1.txt palindromy, p2.txt palindromy cyfrowe na ASCII, p3.txt te słowa, które po wymianie jednego znaku stałyby się palindromem cyfrowym na kodach ASCII
