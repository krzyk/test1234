# Lista 5

Generator haseł

1. Napisz program, który będzie losował określoną liczbę znaków (minimum 8) i utworzy z nich hasło. Znaki losuj wykorzystując kody ASCII. Nie losuj białych znaków!
2. Zmodyfikuj poprzedni program - utwórz funkcję generator\_hasel(int dlugosc), która losuje określoną liczbę znaków podaną jako argument funkcji
3. Zmodyfikuj funkcje generator\_hasel(), która teraz będzie przyjmowała dwa parametry dlugosc oraz dodatkowo typ(int), gdzie:
   - typ=1 to hasło dowolne,
   - typ=2 hasło wymaga przynajmniej jednej liczby i dużą literę,
   - typ=3 -&gt; hasło wymaga przynajmniej jednej cyfry, jednej litery i jednego znaku niealfanumerycznego
4. Wygeneruj 10 haseł wg przepisu w zadaniu 3, dla typu=3 i zapisz je do pliku.

---

Obsługa plików

Korzystając z pliku ABC.txt:

1. Policz, ile w pliku jest słów zaczynających się od litery A
2. Do pliku A.txt przepisz słowa zaczynające się na literę A, do pliku B.txt zaczynające się na B, a do C.txt - na literę C.

Korzystając z pliku TROJKOWE.txt:

1. Przepisz do nowego pliku *z2.txt* te liczby, które mają przynajmniej jedną trójkę w napisie. Zauważ, że liczby są bardzo długie w związku z czym nie możemy ich przechować w typie liczbowym.
2. Zakładając że w pliku zostały zapisane liczby w systemie trójkowym dokonaj ich konwersji na system dziesiętny i przepisz je do pliku *zamienioneTrojkowe.txt*
