# Lista 1

<ol>
<li>Napisz klasę <strong>Tocena</strong>, która będzie miała następujące pola składowe: imie i nazwisko ucznia, przedmiot, wartość oceny oraz nazwę przedmiotu:<ol>
<li style="list-style-type: none;"><ol>
<li>Stwórz dwa obiekty klasy TOcena, przy czym: pierwszemu obiektowi nadaj wartości pól składowych korzystając z operatora ".", a drugiemu nadaj wartości przy użyciu zbudowanej przez Ciebie publicznej metody ustaw()  </li>
<li>Wypisz pola drugiego obiektu na ekran (zbuduj wcześnej odpowiednią metodę).</li>
<li>Następnie zmień pola klasy Ocena na prywatne - co należy zrobić, aby usunąć pojawiające się błędy?<br/><br/></li>
</ol></li>
</ol></li>
<li> Zbuduj klasę <strong>TOsoba</strong> o polach prywatnych: imię, nazwisko, rokUrodzenia, pensja. W programie głównym utwórz obiekt klasy osoba.<ol>
<li style="list-style-type: none;"><ol>
<li>Zbuduj funkcję składową klasy Tosoba o nazwie <code>wypisz()</code> wypisują dane osobowe obiektu klasy Tosoba.  </li>
<li>Zbuduj funkcję <code>ustaw()</code> wypełniającą dane osobowe, wywołaj ją przed metodą <code>wypisz()</code> dla obiektu klasy Tosoba.</li>
<li>Zbuduj funkcję składową <code>ileLat()</code> wypisującą ile lat ma obiekt klasy Tosoba. Zbuduj funkcję składową <code>naEuro() </code> zwracającą pensję w euro, kurs euro przyjmij w parametrze funkcji.Uwaga! W zadaniu 1 i 2 klasy nie wykorzystują konstruktorów, a jedynie metodę ustaw() do wypełnienia danych. Dla klasy Tosoba utwórz konstruktory i poprawnie zbuduj obiekty.<br/><br/></li>
</ol></li>
</ol></li>
<li>Zbuduj klasę<strong> Ttrojkat</strong> o polach prywatnych bok1, bok2, bok3. Utwórz odpowiednie konstruktory a następnie:<ol>
<li>metodę <code>pole()</code> (wykorzystaj wzór Herona -&gt; google),</li>
<li>metodę <code>czyTrojkat()</code> - zwracający typ boolean - sprawdzającą czy z podanych boków da się uzyskać trójkąt,</li>
<li>metodę <code>czyRownoramienny()</code> - void</li>
<li>getery, czyli metody <code>getBok1(), getBok2(), getBok3() </code>- zwracające długości boku - przydatne by dostać długość każdego z boków oddzielnie, a nie jest to możliwe gdy pola bok1, bok2, bok3 są prywatne,</li>
<li>setery <code>setBok1(), setBok2(), setBok3()</code> - pozwalające na przedefiniowanie boku</li>
<li>Zbuduj obiekty klasy Ttrojkat, wywołaj funkcje składowe.<br/><br/></li>
</ol></li>
<li>Zbuduj klasę<strong> TosobaBMI</strong> o polach prywatnych id, wzrost, waga.</li>
</ol>

<ol><ol>
<li style="list-style-type: none;"><ol>
<li>zbuduj stosowne konstruktory</li>
<li>metodę <code>bmi() </code>zwracającą wzkaźnik bmi osoby</li>
<li>metodę <code>figura()</code> opisującą na podstawie bmi() jaka jest figura osoby. Zadbaj o optymalnie napisaną instrukcję if</li>
<li>zbuduj setery i getery, tzn. <code>setWaga(), setWzrost(), getId(), getWaga(), getWzrost()</code></li>
<li>stwórz kilka obiektów klasy OsobaBMI, wywołaj stosowne metody</li>
<li>w programie głównym dla dwóch osób sprawdź która z nich ma niższy wskaźnik <code>bmi()</code></li>
<li>***zbuduj metodę, ktora sprawdza, która z dwóch osób ma niższy wskaźnik BMI (metoda jako parametr przyjmuje JEDEN obiekt klasy OsobaBMI, bo druga osoba to ta dla ktorej wywoływna jest funkcja)</li>
<li>zbuduj konstruktor, ktory na bazie osoby buduje nową osobę (tzn. public OsobaBMI(OsobaBMI o){...}<br/><br/><br/></li>
</ol></li>
</ol></ol>

Zadanie 5:  
W poniższym zadaniu funkcje, które nie są inline umieść poza definicją klasy (w klasie robimy tylko deklaracje, poza klasą - całą definicję odwołując się operatorem zakresu :: do klasy)

1. Stwórz klasę `Tplyta,` a w niej pola:`autor, tytulPlyty, rokWydania.`Pola ustaw prywatne, zbuduj do nich setery i getery, konstruktor z argumentami będącymi polami klasy. Następnie:

- zbuduj metodę `drukujOkladke()`, która będzie wypisywała na ekran `tytul plyty, autora, i rok wydania.`
- Dodaj pole `tytulyPiosenek,` które będzie tablicą łańcuchów znaków. Załóż, że każda płyta będzie miała max 3 piosenki. Do tego pola zbuduj metodę typu void `nagrajPlyte(...)`, która będzie pobierała w argumentach 3 tytuły piosenek, a następnie wpisze je do tablicy `tytulyPiosenek` (zaczynajac od pozycji 0)dodaj metodę `pokazPiosenki()`, która będzie zwracała listę piosenek danej płyty (czyli tablicę tytulyPiosenek)
- stwórz metodę `miksuj()`, która będzie zwracała losową piosenkę (jej tytul) z danej płyty.
- \*\*\*\*\*zbuduj metodę `napiszTekstPiosenki(...)`, która jako argument będzie pobierała ilość liter, a zwracała przypadkowy ciąg małych liter (tyle, ile ich podasz w argumencie metody).
- przetestuj klasę
