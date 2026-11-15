# Instrukcja wyboru switch

## switch

```cpp
    int wybor;
    cout << "Podaj wybor: ";
    cin >> wybor;
    switch( wybor )
    {
    case 2:
        cout << "dwa" << endl;
        break;
    case 1:
        cout << "jeden" << endl;
        break;
    case 3:
        cout << "trzy" << endl;
        break;
    default:
        cout << "ani jeden, ani dwa, ani trzy" << endl;
    }
```

UWAGI:

- default nie jest obowiązkowe
- zmienna wybor może być typu znakowego, wtedy odpowiednio implementujemy case 'a':
- Napisanie switch bez break spowoduje wykonanie wszystkich instrukcji od wskazanego case'a
- switch można zastąpić kilkoma zagnieżdżonymi if-ami, tu:

```cpp
    int liczba;
    cout << "Podaj liczbe: ";
    cin >> liczba;

    if(liczba ==2)
        cout << "dwa" << endl;
    else    
        if(liczba==1)
            cout << "jeden" << endl;
        else
            if(liczba==3)
                cout << "trzy" << endl;
            else
                cout << "ani jeden, ani dwa, ani trzy" << endl;
```
