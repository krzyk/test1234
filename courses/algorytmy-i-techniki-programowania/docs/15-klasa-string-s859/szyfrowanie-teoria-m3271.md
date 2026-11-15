# Szyfrowanie - teoria

*Tekst jawny* - niezaszyfrowana wiadomość  
*Szyfrogram* - zaszyfrowana wiadomość  
<https://zpe.gov.pl/a/przeczytaj/DxwetWxOL>

Podział i krótkie omówienie:

1. Szyfr **podstawieniowy**- każdy tekst znaku jawnego jest zastępowany innym znakiem, np.*szyfr Cezara*
2. Szyfr **przestawieniowy**- w tekście zaszyfrowanym pojawiają się wszystkie znaki tekstu jawnego, ale w innej kolejności (*szyfr płotkowy*), np:  
     
   Tekst jawny: TOBEORNOTTOBETHATISTHEQUESTION  
     
   T O B E O R N O T T  
   O B E T H A T   I  S T  
   H E Q U E S T  I  O N    
     
   Szyfrogram: TOHOBEBEQETUOHERASNTTOIITSTTTN  
     
   PODZIAŁ ze względu na tzw. klucz to:
3. Szyfry **symetryczne**: szyfry, które zarówno do szyfrowania jak i odszyfrowania stosują jeden i ten sam klucz (<https://zpe.gov.pl/a/przeczytaj/DCqLdPDEz>). Dzielą się na:
   1. **Strumieniowe szyfry symetryczne** - generujemy strumień bitów będący kluczem, który następnie wykorzystujemy do szyfrowania tekstu jawnego (zazwyczaj korzysta się z operacji XOR miedzy kluczem a tekstem jawnym
   2. **Blokowe szyfry symetryczne** - tekst jawny dzielimy na bloki, np. po 8 bitów i każdy blok szyfrujemy osobno kluczem
4. Szyfry**asymetryczne** - wiadomość szyfrujemy publicznym kluczem, ale deszyfrowanie odbywa się za pomocą tzw. klucza prywatnego.  
   Klucz szyfrujący jest więc inny od klucza deszyfrującego. Klucz jawny(szyfrujący) możemy udostępnić każdemu, ale klucz deszyfrujący (tajny, prywatny) znany jest tylko odbiorcy wiadomości, np. *algorytm RSA* - powszechnie stosowany w przeglądarkach, wykorzystywany przez serwery, protokole SSL.  
     
   PODZIAŁ ze względu na tzw. alfabet:
5. **Szyfry polialfabetyczne** - ta sama litera w tekście jawnym może być zaszyfrowana na inny sposób w ramach jednego procesu szyfrowania np. raz literę A zamieniamy na E, a innym razem na K (np. szyfr Vigenere'a, Enigma)
6. **Szyfry monoalfabetyczne** -  szyfr, w którym jednej literze alfabetu tajnego odpowiada dokładnie jedna litera alfabetu jawnego (np. szyfr Cezara)

***PRZYKŁAD***  
***Szyfr Vigenere'a - szyfr symetryczny, podstawieniowy**  
**Zaszyfrowanie słowa „JADE” kluczem „BEC” daje słowo „AEFF**”*

<table border="1" cellpadding="0" cellspacing="0" rules="rows">
<tbody border="1">
<tr>
<td valign="top" width="45">
<p>A</p>
</td>
<td valign="top" width="45">
<p>B</p>
</td>
<td valign="top" width="45">
<p>C</p>
</td>
<td valign="top" width="45">
<p>D</p>
</td>
<td valign="top" width="45">
<p>E</p>
</td>
<td valign="top" width="45">
<p>F</p>
</td>
<td valign="top" width="45">
<p>G</p>
</td>
<td valign="top" width="45">
<p>H</p>
</td>
<td valign="top" width="45">
<p>I</p>
</td>
<td valign="top" width="45">
<p>J</p>
</td>
</tr>
<tr>
<td valign="top" width="45">
<p>0</p>
</td>
<td valign="top" width="45">
<p>1</p>
</td>
<td valign="top" width="45">
<p>2</p>
</td>
<td valign="top" width="45">
<p>3</p>
</td>
<td valign="top" width="45">
<p>4</p>
</td>
<td valign="top" width="45">
<p>5</p>
</td>
<td valign="top" width="45">
<p>6</p>
</td>
<td valign="top" width="45">
<p>7</p>
</td>
<td valign="top" width="45">
<p>8</p>
</td>
<td valign="top" width="45">
<p>9</p>
</td>
</tr>
</tbody>
</table>

<table border="1" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td width="110">
<p><strong>pierwsze słowo </strong></p>
</td>
<td width="89">
<p>J</p>
</td>
<td width="79">
<p>A</p>
</td>
<td width="85">
<p>D</p>
</td>
<td width="88">
<p>E</p>
</td>
</tr>
<tr>
<td width="110">
<p><strong>drugie słowo - klucz </strong></p>
</td>
<td width="89">
<p>B</p>
</td>
<td width="79">
<p>E</p>
</td>
<td width="85">
<p>C</p>
</td>
<td width="88">
<p>B</p>
</td>
</tr>
<tr>
<td width="110">
<p><strong>pozycja litery klucza </strong></p>
</td>
<td width="89">
<p>1</p>
</td>
<td width="79">
<p>4</p>
</td>
<td width="85">
<p>2</p>
</td>
<td width="88">
<p>1</p>
</td>
</tr>
<tr>
<td width="110">
<p><strong>szyfr </strong></p>
</td>
<td width="89">
<p><strong>J(9)+B(1) = A(0)</strong></p>
</td>
<td width="79">
<p><strong>A(0)+E(4)=E(4)</strong></p>
</td>
<td width="85">
<p><strong>D(3)+C(2) =F(5) </strong></p>
</td>
<td width="88">
<p><strong>E(4)+B(1)=F(5)</strong></p>
</td>
</tr>
</tbody>
</table>
