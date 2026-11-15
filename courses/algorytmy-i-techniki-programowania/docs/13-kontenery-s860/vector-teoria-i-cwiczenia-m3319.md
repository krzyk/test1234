# vector teoria i ćwiczenia

**vector** to pewna specjalna tablica, która rośnie w ramach dodawania elementów.

W poniższym przykładzie dane jest tablicą liczb całkowitych, ale użycie vector daje nam swobodę dopisywania elementow bez kontroli indeksow,  nie musimy też martwić się o rozmiar

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    //vector<typ> dane;
    vector<int> dane;

 
    //dodawanie elementow:
    dane.push_back(2); //dodanie liczby 2 na ostatnia pozycje tablicy
    dane.push_back(4);
    dane.push_back(1);
         dane.pop_back(); //usunie ostatni element
    
    cout << "tablica dane ma rozmiar " << dane.size()<<endl;
    
    cout<< "tablica dane zawiera wartosci: " <<endl;
    //1 sposób          
    for(int i=0;i<dane.size();i++)
        cout << dane[i]<< " "; //wypisze 2,4,1
    //2 sposób for range
    for (int i: dane)
         cout<<i;

    return 0;
}
```

**Funkcje:**

[**https://www.kompikownia.pl/index.php/2019/04/18/poznaj-nowoczesna-tablice-vector-w-c/**](https://www.kompikownia.pl/index.php/2019/04/18/poznaj-nowoczesna-tablice-vector-w-c/)

- **[push\_b](https://www.kompikownia.pl/index.php/2019/04/18/poznaj-nowoczesna-tablice-vector-w-c/)ack()** - dodaje do końca tablicy nowy element podany w nawiasie
- **begin()** - wskazuje pierwszy element dynamicznej tablicy (cout&lt;&lt;dane.begin(); --&gt; wyświetlanie elementu pierwszego, dane.begin()+1 -&gt; elementu drugiego)
- **end()** - wskazuje na koniec dynamicznej tablicy
- **insert()** - dodaje element do dynamicznej tablicy w podanym miejscu np.: dane.insert(dane.begin(),5);
- **size()** - zwraca ilość elementów tablicy
- **pop\_back()** - usuwa ostatni element
- **erase() -**  usuwa element w konkretnym miejscu, np.: dane.erase(vec.begin()+1) - usuwa element drugi, dane.erase(dane.begin()+2,dane.begin()+5) -&gt; usuwa elementy od tego o indeksie 2 do elementu o indeksie 4 włącznie
- **empty()** - sprawdzić czy obiekt jest pusty
- **at()** - dostęp do konkretnego elementu tablicy, tzn. tablica.at(1) -&gt; tablica[1]

Zwracanie vectora z funkcji:  
vector&lt;int&gt; stworzTablice(int rozmiar) {   
     vector&lt;int&gt; tab(rozmiar);   
      for (int i = 0; i &lt; rozmiar; i++)   
         tab[i] = i;   
      return tab;}  
  
int main() {   
   int size = 5;   
   vector&lt;int&gt; tablica = stworzTablice(size);`}`

Przekazywanie vectora jako parametr funkcji:  
void zmodyfkujTablice(vector&lt;int&gt; &tab) {   
     tab.push\_back(100);  
}  
  
int main() {   
   vector&lt;int&gt; tablica = {1,2,3,4};  
   zmodyfikujTablice(tablica);   
}

**Ćwiczenia:**

<ol>
<li>Wczytaj 10 liczb, a wszystkie te liczby, które są dodatnie wstaw do vectora, a następnie:<ol>
<li>Usun ostatni element z listy</li>
<li>Usun element drugi z listy</li>
<li>Wyswietl vector i podaj liczbe jego elementow</li>
</ol></li>
<li>Wygeneruj vector za pomoca listy inicjalizacyjnej, wpisujac mu wartosci 2,4,8,10 a nastepnie:<ol>
<li>za pomoca fora przechodzacego po kolejnych elementach kolekcji policz srednia elementow tablicy</li>
<li>dodaj 0 na początek vectora</li>
<li>dodaj 20 na trzecią pozycję</li>
</ol></li>
<li>Stwórz vector, do którego wpiszesz 10 kolejnych potęgi liczby 2.</li>
<li>Odgadnij wzór ciagu i wpisz 100 jego elementów do vectora:<br/>1, 2,2,3,3,3,4,4,4,4 ....</li>
<li>Odgadnij wzór ciągu i wpisz 20 jego elementów do vectora<br/>99, 98, 97, 94, 90, 85, .....</li>
<li>Wpisz do pliku tekstowego kilka liczb dodatnich i ujemnych, następnie odczytaj z pliku liczby i do tablicy wstaw tylko te, które są dodatnie</li>
<li>Wpisz do pliku tekstowego kilka liczb, następnie odczytaj z pliku liczby i do tablicy wstaw liczby, ale bez powtórzeń</li>
<li>Wygeneruj plik tekstowy, w którym będziesz  przechowywał dane: data_treningu i 3 długości skoków w dal<br/>np. 12-10-2026 5.5 2.2 5.7</li>
<ul>
<li style="list-style-type: none;">
<ul>
<li>Liczą się tylko te treningi, na których oddano wszystkie skoki odpowiednio dalekie - od 5 metrów.</li>
<li>Podaj najlepszy średni wynik spośród liczących się treningów</li>
</ul>
</li>
</ul>
<li>
<p>Okrąg na płaszczyźnie reprezentujemy za pomocą trzech liczb x, y, r, gdzie x i y to współrzedne środka okręgu, a r promień</p>
<p>Wczytaj dane dla okręgu, a następnie:</p>
<ul>
<li style="list-style-type: none;">
<ul>
<li>
<p>do pliku 1.txt zapisz te dane okręgów, które są całkowicie w 1 ćwiartce</p>
</li>
<li>
<p>do pliku styczne.txt podaj te pary okręgów, które są styczne wewnętrznie/zewnętrznie.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
