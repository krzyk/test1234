# Kontenery

**Kontenery w C++** to gotowe struktury danych z biblioteki standardowej (STL – *Standard Template Library*), które służą do przechowywania wielu elementów (np. liczb, napisów) w uporządkowany sposób.

Aby z nich korzystać, dołączamy odpowiedni nagłówek, np.:

```cpp
#include<vector>
#include<set>
#include<map>
```

Kontenery w C++ ułatwiają przechowywanie i przetwarzanie danych. Najczęściej używany jest `vector`, ale w zależności od potrzeb można wybrać inny typ, np. `map` do przechowywania par klucz–wartość lub `set`, gdy chcemy mieć tylko unikalne elementy.

- są bezpieczniejsze niż zwykłe tablice
- mają wiele zdefiniowanych funkcji ułatwiających ich obsługę
- nie wymagają kontroli i zarządzania pamięcią

Podział kontenerów:

1. Kontenery **sekwencyjne** - przechowują elementy w określonej kolejności,  używamy, kiedy kolejność elementów ma znaczenie (np. `vector, list, array`)
2. Kontenery **asocjacyjne** - przechowują elementy w postaci kluczy, lub pary klucz-wartość (np. `set, map`). Używamy ich kiedy chcemy szybko wyszukiwać po kluczu
3. Kontenery **haszujące** (nieuporządkowane) - podobne do asocjacyjnych, tylko pracują na danych nieuporządkowanych. Bardzo szybkie wyszukiwanie po tablicach haszujących (np. `unordered_set, unordered_map`)
