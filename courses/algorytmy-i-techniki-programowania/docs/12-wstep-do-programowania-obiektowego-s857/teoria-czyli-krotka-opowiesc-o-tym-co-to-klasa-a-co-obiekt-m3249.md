# Teoria, czyli krótka opowieść o tym co to klasa a co obiekt

KLASA to po prostu typ danych, które Ty sam możesz zaprojektować. Przykładowo, takim typem danych może być wymyślony przez Ciebie typ - ***Tsamochod(T od typ)***. Będziemy traktowali go tak samo jak typ danych **int**. Skoro tak, to możemy zapisać, podobnie jak dla typu **int:**

```cpp
int x;
Tsamochod y; //jestem w fabryce, właśnie z niej wyszedł pierwszy egzemplarz klasy Tsamochod o nazwie y
```

y jest teraz OBIEKTEM (instancją, egzemplarzem) klasy Tsamochod. Zastanów się jakimi cechami powinien odznaczać typ - klasa samochód. Może to być kolor, moc, typ silnika itd. Te cechy to tzw. POLA klasy. Ponadto, samochód powinien też coś robić, np. jeździć. Możemy też wydrukować mu kartę pojazdu - a to wszystko przy użyciu specjalnych funkcji - METOD (czyli funkcji, znajdujących się wewnątrz klasy)

```cpp
class Tsamochod{
     public:
       int cena;                    //pole cena klasy Tsamochod
       int moc;
      double przyspieszenie;
```

`void jedz(){` //metoda klasy Tsamochod, czyli po prostu funkcja  
 `cout<<"nic mnie nie zatrzyma! brum brum!";`  
 `}`  
 `void kartaPojazdu(){`  
 `cout<<"moc="<<moc<<"przyspieszenie="<<przyspieszenie;`  
 `}`  
`}`  
  
Jeśli w programie głównym stworze teraz obiekt klasy samochód, np. w ten sposób:

```cpp
Tsamochod z;  //czyli jestem w fabryce i produkuje samochód wg mojego opisu wewnątrz klasy
```

to mogę teraz nadać mu moc, ustalić cenę itd. wykorzystując (np.) do tego operator . :

```cpp
z.moc = 100;
z.przyspieszenie = 6.5;
```

Jeśli chciałabym żeby samochód zaczął jeździć to używam odpowiedniej metody:

```cpp
z.jedz();
```

Podobnie, gdy chce wydrukować moja kartę pojazdu:

```cpp
z.kartaPojazdu();
```

---

**Najważniejsze pojęcia:**

<a id="yui_3_13_0_2_1472644263092_566"></a>

<a id="yui_3_13_0_2_1472644263092_565"></a>**Klasa (class)** - złożony typ danych będący opisem (definicją) pół i metod (funkcji składowych). Klasa jest wzorcem dla obiektu. Obiekt - to reprezentant/przedstawiciel/instancja klasy.

**hermetyzacja, enkapsulacja** - ograniczanie dostępu do pól struktury/klasy z zewnątrz poprzez zastosowanie tzw. **manipulatorów dostępu**: public, private, protected.

**metoda klasy** = funkcja składowa klasy
