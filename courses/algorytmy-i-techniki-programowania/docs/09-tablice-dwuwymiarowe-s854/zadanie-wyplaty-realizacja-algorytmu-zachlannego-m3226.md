# Zadanie wypłaty - realizacja algorytmu zachlannego

**Wypłaty**

Pracownicy pewnego zakładu pracy otrzymują pensje w kwotach będących wielokrotnością 10 złotych. Kasjer, przygotowując wypłatę, przed pobraniem pieniędzy z banku musi obliczyć, ile potrzebuje banknotów o poszczególnych nominałach (10 zł, 20 zł, 50 zł, 100 zł, 200 zł) do zrealizowania wypłaty. Kasjer każdemu pracownikowi chce wypłacić pensję**<u> w możliwie najmniejszej liczbie banknotów</u>**.

Przyjmijmy, że:

- kwoty wypłat dla poszczególnych pracowników są podane w n-elementowej tablicy `wyplaty[],` gdzie n jest liczbą pracowników zakładu.
- nominały banknotów są przechowywane w 5-cio elementowej tablicy `nominaly[]` (pod indeksem 0 znajduje się nominał 200, pod indeksem 1 nominał 100, itd.)

Napisz program obliczania liczby banknotów w poszczególnych nominałach, które kasjer musi wypłacić poszczególnym pracownikom. Wynik obliczeń należy umieścić w tablicy dwuwymiarowej `kasa[][], gdzie każdy wiersz będzie reprezentował jednego pracownika.`

- `kasa[0][0]` - to liczba banknotów 200zł dla pracownika o indeksie 0 (którego wypłata znajdowała się w wyplaty[0]
- `kasa[0][1]` - to liczba banknotów 100zł dla pracownika o indeksie 0
- `kasa[1][0]` - to liczba banknotów 200zł dla pracownika o indeksie 1

Następnie stwórz tablicę `bank[]`, w której umieścisz sumaryczną liczbę banknotów o każdym z nominałów, jakie musi pobrać kasjer z banku, dla wszystkich pracowników firmy (np. `bank[0]` oznacza ile 200zł banknotów potrzebnych jest na wypłaty dla całej firmy)
