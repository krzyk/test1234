# przygotowanie do testu

Co wyświetli program

#include &lt;iostream&gt;

using namespace std;

int f1(int a, int b){

int c;  
 return ++a+b;  
}  
int main(){  
 int x=1;  
 cout&lt;&lt;f1(x,x)&lt;&lt;" ";  
 cout&lt;&lt;x;  
 system("PAUSE");  
return 0;  
}

ew. pytania:

1. czy funkcja coś zwraca?

2. ile argumentów przyjmuje?

3. w jaki sposób przekazywane są argumenty (przez wartość/ referencję czy wskaźnik)?

4. c jest zmienną lokalna czy globalną?

5. a, b są parametrami formalnymi? czy aktualnymi?

6. x jest parametrem formalnym czy aktualnym?

7. aby funkcja f1 zmieniała parametr co należy zmienić?

II. oto przykładowe wywołania funkcji napisz ich nagłówki

np

f();    -&gt;void f(void)

g('s',5);      -&gt;........................

int x=a(2,2,3); -&gt;.............................

float w=sr(1.3,1.1,4); -&gt;......................

III oto nagłówki funkcji zapisz ich przykładowe wywołania

int f2(int a,float c) -&gt;.............// cout&lt;&lt;f2(2,6);

void s(char k, int n) -&gt;...................................

void f3(void) -&gt; ..............................

IV

Co będzie wynikiem funkcji

int g(int x){

return x\*x+5;

}

int g1(int x){

return x;

return x\*x;

}

int g2(int x){

for(int i=0;i&lt;=10;i++){

     x++;

     return x;

}

}

int g3(int x){

if(!(x!=0)) return 5;

else

for(int i=0;i&lt;=10;i++){

     x++;

}

return x;

}
