# Przykład 2 - hermetyzacja, konstruktor kopiujący i destruktor

**Enkapsulacja -** zasada programowania obiektowego, która polega na łączeniu danych i metod w jednej klasie (jak w kapsule).

Hermetyzacja polega na **ograniczaniu bezpośredniego dostępu** do tych danych z zewnątrz poprzez zastosowanie tzw. **manipulatorów dostępu**: public, private, protected.

Mamy trzy rodzaje dostępu do składnika klasy:

1. **`private` -** dostęp tylko dla funkcji składowych danej klasy (i klas *zaprzyjaźnionych*)  
   <u>private jest wartością domyślną</u>
2. **`protected`** - dostęp tylko dla funkcji składowych danej klasy + dla klas *potomnych*
3. **`public -`** dostępny bez ograniczeń

```cpp
class Tpracownik{
    private:
 int lata_pracy;
double pensja;    
public:
Tpracownik(){       //konstruktor bez parametrów
        lata_pracy = 0;
        pensja = 0;
    }
Tpracownik(int l,float p) {  //konstruktor z parametrami
        lata_pracy = l;
        pensja = p;
    }
void setPensja(double p){
     pensja=p;
}
double getPensja(){
     return pensja;
}
void wypisz(){
     cout << "pracownik pracuje " << lata_pracy << " i zarabia " << pensja;
}
    ~Tpracownik(){
    cout<<"działa destruktor";
}
```

```cpp
};
int main() 
{
Tpracownik p1;
Tpracownik p2(3,1500.00);
p1.wypisz();
cout<<p2.getPensja();  //wyświetl tylko pensje obiektu p2
p1.setPensja(2000); //zmień pensje obiektowi p2
p1.wypisz();
p1.lata_pracy=4; //BŁĄD! to jest składnik prywatny!
```

Uwagi:

- `p1, p2` - to obiekty
- konstruktor - funkcja składowa wywoływana podczas tworzenia obiektu klasy, najczęściej służy do inicjowania obiektu
- `p1` - został skonstrowany za pomocą konstruktora bez parametrów
- `p2` - został skonstrowany za pomocą konstruktora z parametrami
- **konstruktor** `Tpracownik()` - <u>ma taka samą nazwę jak klasa, nie ma typu, wywoływany jest niejawnie podczas tworzenia obiektu, konstruktorów może być wiele ale z inną listą parametrów</u> (tzw overloading, przeciążenie nazwy funkcji), jeśli klasa nie ma żadnego konstruktora to wykorzystywany podczas tworzenia obiektu jest konstruktor domyślny bezparametrow
- `setPensja()` - tzw. seter, służy do ustawiania/zmiany wartości pojedynczego pola (w ty przypadku pensji) z zewnątrz klasy
- `getPensja()` - tzw. geter, służy do pobrania wartości pola z zewnątrz klasy

---

**Destruktor**

Destruktor to **specjalna metoda klasy**, która wywoływana jest <u>automatycznie</u> w momencie niszczenia obiektów:

```cpp
~Tpracownik(){
    cout<<"działa destruktor";
}
```

- nosi nazwę klasy z prefiksem ~
- nie zwraca wartości, nie przyjmuje argumentów
- może być tylko jeden w klasie
- wywoływany automatycznie, ale możemy też go wywołać ręcznie (np. kazać mu jednocześnie wykonać jakieś dodatkowe czynności)
- *destruktor przydaje się po to, aby "posprzątać śmieci" przed usunięciem obiektu*

---

**Konstruktor kopiujący**

Konstruktor kopiujący w C++ to specjalny konstruktor, który tworzy nowy obiekt na podstawie już istniejącego obiektu tej samej klasy. Kopiuje wartości jego pól do nowego obiektu.

Jeśli nie zdefiniujemy własnego konstruktora kopiującego, C++ zazwyczaj udostępnia go automatycznie.

```cpp
Tpracownik(const TPracownik &prac) {  //konstruktor KOPIUJACY
        lata_pracy = prac.lata_pracy;
        pensja = prac.pensja;
    }
```

//a następnie w main() mamy:

`Tpracownik p2(3,1500.00);`  //zwykły konstruktor, parametrowy

**`Pracownik p3 (p2);` //konstruktor kopiujący**

****`Pracownik p4 = p2 ;` //konstruktor kopiujący - inna postać**wywołania, częściej spotykana**
