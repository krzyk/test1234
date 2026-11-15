# Zmienne alokowane dynamicznie

**Statyczna alokacja pamięci**(np. `int zmienna;` ) ma przydzieloną pamięć na stosie. Takie przydzielenie panie≥ci realizowane jest podczas kompilacji programu. W trakcie działania programu wielkość stosu się nie zmienia, a pozostała część pamięci operacyjnej dostępna w trakcie działania programu jest nazywana stertą. Sterta może być wykorzystywana na zmienne programowe - wtedy alokacja staje się dynamiczna bo to my w zależności od potrzeby możemy utworzyć nową zmienna, a także zwolnić pamięć przydzieloną do niej.

**Dynamiczna alokacja zmiennych** w C++ polega na przydzielaniu pamięci w trakcie działania programu (czyli **w czasie runtime**), zamiast z góry określonej ilości pamięci w momencie kompilacji. Do dynamicznej alokacji pamięci w C++ używa się operatorów **`new`** i **`delete`**. Alokacja jest dynamiczna, ponieważ to my decydujemy w jakiej chwili chcemy tworzyć a w jakiej niszczyć pamięć.

```text
int* ptr = new int;  // Alokacja pamięci dla jednej zmiennej typu int   
*ptr = 5;  // Przypisanie wartości
```

```text
*ptr = *ptr + 5;  // używanie zmiennej
```

```text
delete ptr;  // Zwolnienie pamięci
```

```text
int* ptr2 = new int(10); //Alokacja z inicjalizacją
```

---

**Zadanie:**

Napisz program umożliwiający dla prostopadłościanu o bokach a, b, c obliczenie objętości, pola powierzchni bocznej prostopadłościanu. Dynamicznie zaalokuj pamięć dla boków, przy czym wartości pobierz na różne sposoby: wczytaj, wylosuj, zainicjalizuj przy deklaracji. Pamiętaj o zwalnianiu pamięci.
