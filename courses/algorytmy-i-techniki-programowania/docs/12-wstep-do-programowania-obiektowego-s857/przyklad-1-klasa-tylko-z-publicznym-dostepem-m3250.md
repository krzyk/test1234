# Przykład 1 - klasa tylko z publicznym dostępem

Przykład 1:

```cpp
#include<iostream>
using namespace std;

class Tsamochod{
    public:
 int przebieg;   //POLA = SKŁADNIKI KLASY
int cena;   
string marka;
void wypiszPola(){  //METODA
     cout << marka << " z roku " << rokProdukcji << "kosztuje"<<cena;
}
    int rokProdukcji;   // składniki klasy można umieszczać w dowolnym miejscu wewnątrz klasy,  ale będą znane w całej klasie

    void zmienPrzebieg(int ile){
                  przebieg=przebieg-ile;
    }
};
int main() 
{
Tsamochod s1;    //s1 to obiekt klasy Tsamochod, nasz pierwszy egzemplarz
s1.rokProdukcji=2020;   //ustawiamy pola (cechy) naszego obiektu 
s1.cena=80000;
s1.marka="honda";
s1.wypiszPola();
    Tsamochod s2;  //s2 drugi egzemplarz klasy
    s2.rokProdukcji=2010;
    s2.cena=15000;
    s2.marka="honda";
    s2.przebieg=200000;
    s2.zmienPrzebieg(50000); //przekręcamy licznik
```

`s2.wypiszPola();`  
`}`  
  
Uwagi:

- `s1, s2` - to obiekty
- obiekt - to reprezentant/przedstawiciel/instancja klasy Tsamochod
- `s1, s2 mają ustawiony publiczny dostęp (public:), tylko dlatego możemy ustawić pola za pomocą operatora dostępu . (s1.cena = )`
- składniki klasy można umieszczać w dowolnym miejscu, a i tak znane są w całej klasie. Klasa to takie pudło na składniki (w przeciwieństwie do funkcji) - nie ma początku ani końca.
- "kapsułowanie" (encapsulation) - umieszczanie w ciele klasy danych i funkcji; w tej definicji klasy  jak w kapsule zamknięte są dane oraz funkcje potrzebne do posługiwania się klasą
- czasami składnikom można przypisywać wstępne wartości (jest to tzw. inicjalizacja w klasie), np. w sytuacji gdyby nasza klasa obsługiwała pionki do gry i należałoby umieścić pionka w odpowiednim, początkowym miejscu:

```cpp
class Tpionek{
      int pozycjaX=1;  //lub w w wersji C++111: int pozycja{1};
      int pozycjaY=1;    
}
```
