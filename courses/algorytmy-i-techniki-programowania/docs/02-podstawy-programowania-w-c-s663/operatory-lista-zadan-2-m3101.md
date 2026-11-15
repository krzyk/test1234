# Operatory - lista zadań 2

1. Jaką wartość przyjmą zmienne po wykonaniu poniższych instrukcji a)-f)? Startowe wartości zmiennych wyglądają zawsze następująco:  
     
   int x=10, y=4, z=5;  
   float a;  
     
   a)  x=y++;     //x=?  
   b) x\*=y\*2;    //x=?   
   c) a = x/3;    //a=?  
   d) a = x/3.;  
   e) a = (float)x/3;  
   f) y = (float)x/3;   //y=?
2. Jaką wartość przyjmie zmienna oblicz typu bool dla następujących danych:  
     
   `int a = 1, b= 10, c = 100;`  
     
   a) `oblicz = a < b && b <c II a==b;`  
   b) `oblicz = a<b and (b<c or a==b);`   
   c) `oblicz = "ala ma kota" and 0;`  
   d) `oblicz = 5 and "0";`
3. Jaką wartość przyjmą zmienne po wykonaniu poniższych instrukcji a)-d)? Startowe wartości zmiennych wyglądają zawsze następująco:  
     
   `int x=1, y=4, z=2;`  
     
   `a) bool wynik = x++>2 && y++ >=2;`  
   `b) bool wynik = ++x>2 || y++ >=2;`  
   `c) bool wynik = x++>1 && y++ == 4 && z-->0;`  
   `d) int wynik = ++x - x*y;`
4. \*\*Jaka będzie wartość zmiennej wynik po zastosowaniu operatorów bitowych, jeżeli  początkowa wartość zmiennej x wynosi 7? (bitowo:  0000 0000 0000 0111 - zapisane na 2 bajtach, czyli 8 bitach)  
     
   `unsigned short x = 7;`  
     
   a) `wynik = x | x;`  
   b) `wynik = ~x;`  
   c) `wynik = x&x;`  
   d) wynik = x&gt;&gt;1
