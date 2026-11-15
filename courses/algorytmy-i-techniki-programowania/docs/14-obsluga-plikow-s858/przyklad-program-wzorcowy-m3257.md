# Przykład - program wzorcowy

## Przykładowy program z komentarzem

```cpp
#include <iostream>
#include <fstream> 

using namespace std;

int main(){
```

`ifstream wejscie("liczby.txt");` //i jak input - wejście-odczyt  
    `ofstream wyjscie("wynik.txt");` // o jak output - wyjście-zapis  
      
    //zabezpieczenie, czy plik istnieje - można pominąć            
 `if(!wejscie){`   
 `cout << "pliku nie mozna otworzyc" << endl;`   
 `return 1;`   
 `}`   
  
    //zakładamy, że w pliku znajdują się liczby całkowite, które wczytujemy po jednej    
    int n;

```cpp
     //jeśli chcemy wczytywać po dwie liczby, to deklarujemy int a,b; i wczytujemy wejscie>>a>>b;                                         
    
    while(wejscie>>n){       //wczytanie z pliku; zauważ, że wygląda podobnie do cin>>n, jeśli nie ma nic już do wczytania to petla przestaje działać

         cout << n <<endl; //to co wczytuje w warunku wypisuje na ekran
         wyjscie << n<<endl; //zapis do pliku, zauważ, że wygląda podobnie do cout<< n     
    }
    //zamknięcie plików
    wejscie.close();
    wyjscie.close();
```

   //jeśli chcemy ponownie użyć tych samych obiektów do obsługi innych plików to je ponownie otwieramy tak jak poniżej, ale później musimy je znowu zamknąć  
 `wejscie.open("plik2.txt");`  
 `wyjscie.open("plik3.txt");`

`return 0;`  
`}`  
  
**UWAGA**:nie ma znaczenia w tej metodzie jak zapisane są liczby w pliku, mogą być rozdzielone enterem, spacją, mogą być zapisane nieregularnie.
