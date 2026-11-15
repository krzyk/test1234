# Lista 2

1. Zbuduj klasę **Tdom**, a w nim ustaw następujące pola: `id,` `powierzchnia, cena, liczbaPokoi`. Następnie:
   1. dla każdego z pól zbuduj getery i setery.
   2. zbuduj konstruktor z parametrami ustawiający wartość wszystkich pól
   3. przeciąż poprzedni konstruktor i zbuduj taki, który ustawia tylko powierzchnię i cenę
   4. zbuduj metodę `promocja()`, która będzie zmieniała cenę domu w zależności od procenta, jaki poda się w argumencie funkcji
   5. w funkcji `main()` stwórz i przetestuj dwa przykładowe obiekty klas`y dom`
   6. zbuduj funkcję, która będzie pobierała porównywała ceny dwóch obiektów klasy dom i wyświetlała który z nich jest droższy. Funkcję deklaruj wewnątrz klasy, ale zdefiniuj poza nią. Pamiętaj o użyciu operatora zakresu ::
   7. zmień pole id -&gt; ustaw jako statyczne. Co należy zmienić w programie aby wszystko działało poprawnie?
2. Zbuduj klasę **Tmotor**, a w nim ustaw takie pola, jakie uważasz za trafne (minimalnie 3). Następnie:
   1. zbuduj konstruktor z parametrami ustawiający wartość wszystkich pól
   2. zbuduj metodę, która sprawdza stan paliwa w konkretnym obiekcie klasy `motor`
   3. zbuduj funkcję, która jeśli stan paliwa jest mniejszy od 3litrów wyświetla informacje "jedź na stację"
   4. w funkcji `main()` stwórz i przetestuj dwa przykładowe obiekty klasy `Tmotor`
3. Napisz program, który tworzy klasę **Trachunek** o polach: `data, netto, podatek, brutto, nr_rachunku.`
   1. Pola ustaw, aby miały domyślną wartość; konstruktory ustaw jako publiczne, nr\_rachunku powinien być zmienną statyczną
   2. Stwórz dwa przykładowe rachunki (dwa obiekty tej klasy)
   3. Napisz funkcję składową, która oblicza wartość podatku oraz wartość brutto dla stawki 23%.
   4. Napisz funkcję, która "drukuje" wybrany rachunek (wypisuje jego zawartość w "ładny sposób" (niczym wydruk z drukarki)
