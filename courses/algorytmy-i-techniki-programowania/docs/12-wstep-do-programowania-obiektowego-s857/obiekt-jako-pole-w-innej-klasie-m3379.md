# Obiekt jako pole w innej klasie

Bardzo często zachodzi potrzeba, aby wykorzystać jedną klasę do stworzenia pola w innej klasie. Przykładowo, taka klasa jak Data, w której podaje dzień miesiąc oraz rok może być wykorzystywana w różnych okolicznościach - jako data rejestracji czy data urodzin pracownika czy ucznia.

Konstrukcja wtedy wyglada następująco:

class Data{

public:

Data(){     //konstruktor domyślny jest konieczny

dzien=1;

miesiac=1;

rok=1970;

}

Data(int dzien, int miesiac, int rok){

             this-&gt;dzien=dzien;

this-&gt;miesiac=miesiac;

this-&gt;rok=rok;

}

int getDzien(){

return dzien;

}

void wypiszDate(){

cout&lt;&lt;dzien&lt;&lt;"."&lt;&lt;miesiac&lt;&lt;"."&lt;&lt;rok&lt;&lt;endl;

}

private:

int dzien, miesiac, rok;

};

// A TERAZ WYKORZYSTANIE W INNEJ KLASIE - zwróć uwagę na konstruktory:

class Uczen{

public:

Uczen(string imie, int dzien, int miesiac, int rok){

this-&gt;imie=imie;

data\_urodzenia=Data(dzien, miesiac, rok);

}

Uczen(string imie, Data data\_urodzenia){

this-&gt;imie=imie;

this-&gt;data\_urodzenia=data\_urodzenia;

}

void wypiszUcznia(){

cout&lt;&lt;imie&lt;&lt;", ur. dn. ";

data\_urodzenia.wypiszDate();

}

private:

Data data\_urodzenia;

string imie;

};

int main(){

Uczen u1("Ada", 16, 12, 2005);

u1.wypiszUcznia();

Data d1(16,7,2009);

Uczen u2("Hela", d1);

u2.wypiszUcznia();

}
