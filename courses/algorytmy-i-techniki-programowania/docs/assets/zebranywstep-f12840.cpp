#include<iostream>   //dolaczam biblioteke aby obsłuzyc wypisywanie i wczytywanie z ekranu
#include<cmath> //dolaczam biblioteke matematyczna, bo bede korzystac z funkcji matematycznej pow() i sqrt()
using namespace std; //uzywam przestrzeni std, w ktorej znajduje sie cout i cin

int main()
{
	//dopiero w tym miejscu zaczynamy pisac program - nie przed main!
	short a, b;   //deklaracja zmiennej czyli rezerwacja dla zmiennych pamieci
	int x, y;        //dla zmiennej int oznacza zarezerwowanie 4B pamieci, dla short tylko 2 bajty

	//a=50000;  //ta liczba jest za duza dla rozmiaru short!
	a=50;
	a+=10; //to samo co a=a+10   -->> ta linijka oznacza dodanie do zmiennej a 10, a nastepnie przypisanie tej wartosci do a
    cout<<"a="<<a<<endl;   //endl to enter 
	/*uwaga! przy wypisywaniu coutem tekst czyli "blabla" oddzielamy od
	listy zmiennych znakami <<   */

	cout<<"Podaj b ";
	cin>>b;
    
	b++; //inkrementacja; czyli zwiekszam zmienna b o 1.
	cout<<"b="<<b<<endl;

    //moge jednoczesnie zadeklarowac zmienna i przypisac jej wartosc:
	short c=1; //deklaruje zmienne w dowolnym miejscu w programie, najlepiej tuz przed uzyciem
	c--; //dekrementacja, czyli c=c-1
	cout<<"c bylo rowne 1, a po dekrementacji wynosi "<<c<<endl;

    //  % to operator modulo, ktory oblicza reszte z dzielenia, np:
    cout<<"8%3="<<8%3<<endl;
    
	//oblicze pierwiastek ze zmiennej a:
    float pierwiastekZa = sqrt(a);  //piewiastek musi byc typu zmiennoprzecinkowego!!!
	cout<<"Pierwiastek z liczby a ="<<a<<" wynosi "<<pierwiastekZa<<endl;

	//funkcja potegujaca
	cout<<"3 do potegi 4 wynosi "<<pow(3,4)<<endl;




	return 0;//funkcja glowna zwraca 0,jak zadziala prawidlowo, za ta linijka nic nie piszemy!!!
}
