#include<iostream>
using namespace std;

int main()
{
    int tab[8][8];
    
    //przygotowanie pustej szachownicy
    for (int i=0;i<8;i++)
        for (int j=0;j<8;j++)
            tab[i][j]=0;
            
    cout << "podaj pole na którym stoi hetman" << endl;
    int x,y;
    cin>> x >> y;
    int pozycjax=x;
	int pozycjay=y; 
 
    
    
    //atak hetmana po prostej
    
    for(int i=0;i<8;i++)
            {
                        tab[i][y]=1;  //w pionie
                        tab[x][i]=1;  //w poziomie
            }
        
           
    // atak hetmana po skosie
    
    for (int i=0;x+i<8 && y+i<8;i++)
        
        tab[x+i][y+i] = 1;
     
       
    for (int i=0;x-i>=0 && y-i>=0 ;i++)
    
        tab[x-i][y-i] = 1;  
       
        
        
 
                 
    //atak hetmana po drugim skosie
    
    for (int i=0;y+i<8;i++)
        tab[x-i][y+i]=1;                                      
                                          
     for (int i=0;y-i>=0;i++)
        tab[x+i][y-i]=1;
     
            
    
    
    //ustawienie hetmana
    
    
    tab[pozycjax][pozycjay]=2;
    
    //wypisanie planszy
    
    for (int i=0;i<8;i++)
        {
        for(int j=0;j<8;j++)
                cout << tab[i][j]  << "\t";
          cout<<endl<<endl;      
        }
    
    
  
    return 0;
    
}
