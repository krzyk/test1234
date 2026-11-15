# Przykład 4 - statyczny składnik klasy

**Statyczny składnik klasy (pole)** w C++ to taki, który jest <u>wspólny dla wszystkich obiektów klasy</u><u>.</u> Należy do klasy, a nie do konkretnego obiektu. Dzięki temu wszystkie instancje mają dostęp do jednej współdzielonej zmiennej. Aby taką zmienną ustawić dodajemy przedrostek static przed nazwą zmiennej.

```cpp
class Student {
   private:
            string name;

   public:
            static int licznik;    //statyczny składnik może być publiczny lub prywatny

            Student(string n) {
                              n=name;
               licznik++; // przy każdym nowym obiekcie zwiększamy licznik
             }
           ~Student() {
               counter--; // przy usunięciu obiektu zmniejszamy licznik
```

`static int getLicznik(){` //jak składnik statyczny prywatny, tworzymy metodę statyczną zwracającą go, dla publicznego ta metoda niepotrzebna   
                 `return licznik;`  
 `}`

```cpp
};
```

// Definicja i inicjalizacja statycznego składnika musi nastąpić poza klasą  
`int Student::licznik = 0;`

```cpp
int main() {
 cout << "Aktualna liczba studentów: " << Student::licznik << endl; //lub: Student::getLicznik();
Student s1("Ala");
 Student s2("Olek");
cout << "Aktualna liczba studentów: " << Student::getLicznik() << endl;
//można tez tak:
cout<<s1.licznik; lub s2.licznik;
s1.~Student();
cout << "Aktualna liczba studentów: " << Student::licznik << endl;
}
```

Uwaga!

**Statyczny składnik klasy** zazwyczaj jest publiczny. Inicjalizujemy go zawsze poza klasą (przypisujemy wartość). Statyczny składnik to taka wspólna zmienna dla wszystkich obiektów w klasie. Dlatego możemy się do niego odwoływać na kilka sposobów:

`cout<<nazwaKlasy::nazwaSkladnika;`  
lub   
`cout<<nazwaObiektu.nazwaSkladnika;`  
lub  
`cout<<nazwaKlasu::nazwaFunkcjiStatycznejZwracajacejSkladnik;`

---

**Statyczna funkcja składowa**

Statyczna metoda należy do **klasy**, a nie do obiektu. Nie ma dostępu do `this` ani do pól niestatycznych, ale może korzystać ze składników statycznych.

Jeżeli w klasie mamy funkcję, która pracuje tylko na statycznych składnikach to MOŻEMY zadeklarować ją jako statyczną (patrz funkcja getLicznik()).

 Możemy sobie np. zdefiniować funkcję, która właśnie działa w sposób statyczny - nie pracuje na konkretnych obiektach, tylko działa na klasie, np:

```cpp
class Matma{
        static int większą(int a, int b){
              return (a>b)?  a :  b ;
};
int main(){
    cout<<Matma::wieksza(5,10);
}
```
