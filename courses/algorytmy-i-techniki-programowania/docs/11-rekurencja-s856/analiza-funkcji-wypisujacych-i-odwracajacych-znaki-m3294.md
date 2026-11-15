# Analiza funkcji wypisujacych i odwracających znaki

Przeanalizuj funkcje a następnie:

- określ zakończenie wywołań rekurencyjnych
- określ jej działanie

//Funkcja 1:

```cpp
void funkcja()
{
      char znak;
      cout << "podaj znak";
      cin >> znak;
      if (znak != '.'){
              funkcja();
              cout << znak;
       }
}
```

//Funkcja 2: (co wyświetli się dla wywołania w main druk(5) ?

```cpp
void druk(int n){
     if (n>0){
          cout << n+2;
          druk(n-2);
     }
}
```
