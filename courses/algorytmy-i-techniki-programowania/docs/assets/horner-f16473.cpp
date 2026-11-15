//algorytm: znajdowanie wartosci wielomianu za pomoc¹ schematu hornera
//operacja dominujaca w algorytmie: mnozenie
//zlozonosc: lionowa
//program zrealizowany na tablicy z dynamiczn¹ alokacj¹ pamiêci
//schemat hornera wykorzystuje sie do zamiany liczb z innego systemu liczbowego na dziesietny

#include<iostream>
#include<string>
using namespace std;

int main()
{
	cout << "podaj stopien wielomianu: ";
	int n;
	cin>>n;
	
	
	int *w = new int[n+1];
	cout << "podaj wspolczynniki wielomianu zaczynaj¹c od tego przy najwiekszej potedze: "<<endl;
	for(int i=0;i<n+1;i++)
			cin>>w[i];
			
	cout << "oto twoj wielomian: "<<endl;
	
	for(int i=0;i<n+1;i++)
		cout << w[i]<<"*x^"<<n-i<<"+";		
		
	cout << endl << "podaj x dla korego chcesz znalezc wartosc wielomianu: "<<endl;
	float x;
	cin>>x;
	
	float wynik=w[0];
	for(int i=1;i<n+1;i++)
		wynik = wynik*x+w[i];
		
	cout << "wartosc wielomianu wynosi "<<wynik<<endl;	
	
	delete [] w;
    
	cout << endl<<"WYKORZYSTANIE SCHEMATU HORNERA DO ZAMIANY LICZB W INNYM SYSTEMIE LICZBOWYM NA DZIESIETNY" <<endl;	
	
	string liczba;
	int podstawa;
	
	cout << "podaj liczbe i podstawe jej systemu liczbowego: ";
	cin>>liczba;
	cin>>podstawa;
	
	int rozmiar=liczba.size();
	
	int wynikk=(int)liczba[0]-(int)'0';
	
	for(int i=1;i<rozmiar;i++)
		wynikk=wynikk*podstawa+(int)liczba[i]-(int)'0';
		
	cout << "po zamianie liczby "<<liczba<< " z systemu o podstawie "<<podstawa;
	cout <<" na system dziesiatkowy otrzymuje liczbe " <<wynikk; 
	
}
