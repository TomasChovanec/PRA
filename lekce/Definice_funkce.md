# Definice vlastní funkce v jazyce C 
Funkce v jazyce C slouží k rozdělení programu na menší, přehlednější části, které lze znovu použít.

Hlavní výhody funkcí:
- Zjednodušují kód – program je přehlednější a lépe organizovaný.
- Umožňují opakované použití kódu – stejnou funkci lze volat vícekrát, čímž se snižuje duplicita.
- Usnadňují ladění a údržbu – chyby se hledají snadněji, protože jsou izolovány v konkrétní funkci.
- Podporují modulární programování – umožňují rozdělit kód na logické bloky, což zlepšuje strukturu programu.

Funkce mají název, mohou (ale nemusí) přijímat argumenty a vracet hodnotu.

### Funkce bez parametru a návratové hodnoty
Vytvoříme jednoduchou funkci. Klíčové slovo void před názvem funkce označuje, že funkce nevrací žádnou hodnotu. ```void```v závorkách pak znamená, že funkce nepřijímá žádné vstupní argumenty.

```c
void pozdrav(void)
{
    Serial.println("Dobrý den!");
}

void setup() {
    Serial.begin(9600);
}

void loop() {
    pozdrav();
    delay(1000);
}
```

### Funkce s parametrem
Funkce může mít libovolný počet vstupních parametrů (také nazývaných argumenty), které se zapisují do závorek při její definici. Parametry umožňují funkci přizpůsobit její chování podle konkrétních hodnot. Příklad: Pokud chceme aby funkce z předchozího příkladu pozdravila s oslovením jménem, přidáme do funkce parametr ```jmeno```, který následně použijeme v těle funkce. Při volání funkce pak tento parametr předáme s konkrétní hodnotou.

```c
void pozdrav(char jmeno[]) {
    Serial.print("Dobrý den ");
    Serial.print(jmeno);
    Serial.println("!");
}

void setup() {
    Serial.begin(9600);
}

void loop() {
    pozdrav("Horymíre");
    pozdrav("Petro");
    delay(1000);
}

```

### Návratová hodnota funkce
Funkce může také vracet hodnotu. Vytvořme například funkci, která spočítá obsah obdélníku. Tento výsledek ale nebudeme pouze vypisovat přes sériovou linku, ale chceme ho použít v dalších výpočtech. Proto jej místo vypsání vrátíme jako návratovou hodnotu. Funkce vrací hodnotu pomocí příkazu ```return```, který zároveň ukončí její vykonávání. Kód za příkazem ```return``` se již neprovede. Při definici funkce je nutné uvést datový typ návratové hodnoty.

```c
int obsah_obdelniku(int sirka, int vyska)
{
    int vysledek = sirka * vyska;
    return vysledek;
}

void setup() {
    Serial.begin(9600);
}

void loop() {
    int sirka = 5;
    int vyska = 10;
    int obsah = obsah_obdelniku(sirka, vyska);
    Serial.print("Obsah obdélníku: ");
    Serial.println(obsah);
    delay(1000);
}
```

## Úkoly
1. Vytvořte funkci pro blikání LEDkou ```void blikej(int pocet_bliknuti)``` Aby například kód ```blikej(5);``` bliknul 5x LEDkou na pinu 13. Periodu blikání nechám na vás.
2. Pro snadnější práci s ultrazvukovým senzorem vytvořte funkci ```zmer_vzdalenost()```, která bude vracet délku v centimetrech.


### [Zpět na obsah](../README.md)
