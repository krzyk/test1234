# Podsumowanie wiadomości - if, inkrementacja, dekremantacja, wartość logiczna wyrażenia

<a id="yui_3_13_0_2_1516092332411_409"></a>

<a id="yui_3_13_0_2_1516092332411_408"></a>

<a id="yui_3_13_0_2_1516092332411_407"></a>

<a id="yui_3_13_0_2_1516092332411_406"></a>1. Rożne zapisy działań:
   <a id="yui_3_13_0_2_1516092332411_405"></a>
   - czy zapis x=x+5; a x+=5 to jest to samo?
   <a id="yui_3_13_0_2_1516092332411_404"></a>- zapisz inaczej instrukcje:
     <a id="yui_3_13_0_2_1516092332411_403"></a>
     <a id="yui_3_13_0_2_1516092332411_402"></a>- <a id="yui_3_13_0_2_1516092332411_401"></a>`x=x-5;`
     - `x=x/(4-y);`
2. inkrementacja, dekrementacja, kolejność wykonywania instrukcji
   - czy instrukcja `a++, ++a i a=a+1` to jest to samo?
   - czy instrukcja `a--, --a i a=a-1` to jest to samo?
   - co wypisze się na konsoli
     - `a=3; cout << a++;`
     - `a=3; cout << ++a;`
     - `a=1; b=2; c= ++a + b--; cout << a << " " << b << " " << c;`
     - `a=1; b=2; b+=a++; cout << b; cout <<a;`
<a id="yui_3_13_0_2_1516092332411_415"></a>3. Wartość logiczna wyrażenia.
   <a id="yui_3_13_0_2_1516092332411_414"></a>
   - Znajdź wartość logiczną następujących wyrażeń:
     - 7&gt;10 && 1
     - `„Ala” || !5`
   - czy poprawne są następujące zapisy i co ewentualnie się wypisze:
     - `if("ala") cout << ":)";`
     - if(!0) cout &lt;&lt; ":)"; else cout &lt;&lt; ":(";
