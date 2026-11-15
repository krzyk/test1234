# Przestarzałe tablice znakowe char[] - teoria i zadania

**Tablica znakowa (napis)** to sposób zapisu tekstu w stylu C, ale dostępny w C++.  
Jest to tablica typu `char`**zakończona znakiem `'\0'`** (znak końca tekstu). Taką tablicę możemy zadeklarować/zainicjować na kilka sposobów:

char n1[]="ola";  
char n2[4]={'o','l','a','\0'};  
char n3[4]={'o','l','a',null};  
`char n3[3]={'o','l','a'};` //zapis jest prawidłowy, ale nie tworzy napisu, tylko tablicę przechowującą pojedyncze znaki

- napis n1[] to skrócona poprawna forma tworzenia napisu, rozmiar dobiera się sam
- znak '\0' oznacza znak końca napisu i jest on NIEZBĘDNY do prawidłowej obsługi napisów, zatem najbardziej typową tablicą znakową jest tablica n2[]. n2[] ma trzy litery, ale jej rozmiar to 4, bo musi posiadać znak końca napisu
- napis n3[] to inny sposób utworzenia napisu
- napis n4[] jest niepoprawny - nie jest napisem, a jego poprawne działanie jest przypadkowe

Aby bez pętli wczytać i wypisać cały napis możemy go potraktować podobnie jako string, np:

```cpp
char n1[4];
cout << "podaj imię trzyliterowe";
cin >> n1;
cout << "podales imie" << n1;
```

Podstawowe funkcje (użyj biblioteki cstring):

- `strlen()` - liczba liter (bez znaku '\0')
- `strcpy(do_czego, skąd)` -  kopiowanie, np strcpy(n5,n1); --&gt; od teraz w n5 siedzi napis z n1
- `strcat(do_czego_doklejamy, co_doklejamy)` - łączenie łańcuchów , np. strcat(n1,n2); -&gt; w napisie n1 jest stary napis+napis n2   
    
  UWAGA!    
  `char napis[]="abc";`  
  `cout<<strlen(napis); //długość napisu, bez \0 - czyli 3`  
  `cout<<sizeof(napis);`   //ilość zajętej pamięci, czyli razem ze znakiem \0 - wyświetli 4

***Tablice znakowe stosuje się w sytuacji programowania niskopoziomowego, współpracy z bibliotekami języka C.***  
***My jednak będziemy w przyszłości wykorzystywać nowoczesną i zalecaną klasę string do obsługi (tablice znakowe typu char[] są mało bezpieczne, nie mamy nad nimi kontroli rozmiaru itd.)***

---

**Zadanie:** Utwórz dwie tablice znakowe w których przechowasz imię i nazwisko osoby. Obie tablice zainicjuj na stałe wartościami:

```cpp
char imie[]="kamil";
char nazwisko[]={'n','o','w','a','k','\0'};
```

wykonaj następujące polecenia:

- wypisz dane osobowe osoby
- stwórz tablicę inicjaly[] i zapisz w niej inicjały z kropkami (zastanów się jaki będzie rozmiar tej tablicy - nie zapomnij o znaku końca napisu)
- sprawdź, czy osoba jest kobietą - kończy się na litere 'a'
- utwórz kod do banku: 3 litery imienia i 3 nazwiska
- wczytaj swoje nazwisko, sprawdź ile ma liter korzystając z operatora sizeof, pamiętaj, że długość napisu jest o jeden większa
