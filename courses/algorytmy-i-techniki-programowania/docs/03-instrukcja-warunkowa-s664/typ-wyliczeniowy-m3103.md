# Typ wyliczeniowy

## Enum

Typ wyliczeniowy nie należy do typów podstawowych, tylko do typów definiowanych przez użytkownika, ogólna postać wygląda następująco:

```cpp
enum nazwa (identyfikator1, identyfikator2, ...);
```

Identyfikator to tzw. enumerator. Każdemu enumeratorowi odpowiada unikatowy numer (domyślnie 0, 1, 2, itd - chyba że podano inaczej)

Przykład 1:

```cpp
enum ocena{
      ndst = 1,
       dop = 2,
       dst = 3,
       db = 4,
       bdb =5
};
ocena ocJasia = dop;
cout<<"Jasiu dostał"<<ocJasia; //wyświetli 2
```

Przykład2:  
Typ wyliczeniowy można połączyć rownież z instrukcją wyboru switch:

`enum Level {easy, normal, hard} poziom; //można od razu zadeklarować zmienna typu Level ->poziom`   
  
`switch(poziom) {`   
 `case easy : cout << "Wybrałeś łatwiznę --> włączam!";`   
      break;  
    case normal: [cout](http://en.cppreference.com/w/cpp/io/cout) &lt;&lt; "Wybrales tryb średni --&gt;włączam!";   
     break;   
     case hard : [cout](http://en.cppreference.com/w/cpp/io/cout) &lt;&lt; "Przygotuj się na masakrę!";  
     break;  
`}`
