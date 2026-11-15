# Pęla while, do-while - teoria

**Iteracja** - powtarzanie tego samego ciagu instrukcji.

## Składnia:

### while

```cpp
while (warunek) instrukcja;
```

jeśli w pętli wykonuje się więcej instrukcji używamy nawiasów {}:

```cpp
while (warunek) {
          instrukcja1;
              instrukcja2;
          .....
}
```

### do-while

```cpp
do 
    instrukcja;
while(warunek);
```

jeśli w pętli wykonuje się więcej instrukcji używamy nawiasów {}:

```cpp
do {
    instrukcja1;
    .....
}
while (warunek);
```

## Różnice:

1. while sprawdza warunek na początku, do-while na końcu
2. do-while zawsze wykona sie przynajmniej raz, z while może się nie wykonać ani razu

**Wszystkie pętle w C/C++ działają dopóki warunek jest prawdziwy.**
