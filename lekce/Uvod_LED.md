# Úvod do Arduina

### Cíle lekce
- Vysvětlit, co je Arduino, k čemu ho můžeme použít
- Umět použít piny Arduina jako **výstupy** a pomocí funkce ```digitalWrite()``` blikat LEDkou.
- Umět použít piny Arduina jako **vstupy** a pomocí funkce ```digitalRead()``` číst stav tlačítka.
- Umět použít nepájivé pole k propojení součástek a Arduina


## Co je to Arduino?
Arduino je platforma pro výuku a vývoj elektronických projektů. Z hardwarového pohledu je to deska s procesorem, ke které můžete připojit různé senzory, motory, světla a další komponenty, a poté je ovládat pomocí kódu. Programování probíhá v jednoduchém jazyce a jsou k dispozici spousty hotových knihoven, což Arduino činí ideálním nástrojem pro začátečníky i pokročilé, kteří se chtějí naučit základy elektroniky a programování. Arduino se používá ve spoustě projektů, od domácí automatizace po robotiku.

## Hardware
Existuje mnoho typů Arduino desek s různými mikrokontrolery - liší se výkonem, počtem pinů, možnostmi WiFi, Bluetooth atd. V našich hodinách budeme používat Arduino UNO s procesorem ATmega 328.

<img src="../img/01_Uvod_LED_1.png" width="600"/>

## Princip fungování embedded systémů
Slovo „embedded“ znamená, že jde o systémy, které jsou součástí nějakého zařízení, například mikrokontrolér v ledničce, autě nebo robotu, který vykonává specifické úkoly.

![image](../img/01_Uvod_LED_2.png)

## Příklad projektu s Arduinem
Dokážete při pohledu na obrázek popsat, k čemu tento projekt slouží a jaký asi program běží v Arduinu?

<img src="../img/01_Uvod_LED_3.png" width="600"/>


## Psaní programu pro Arduino - funkce setup() a loop()
```C
//sem prijde vlozeni knihoven, inicializace proměnných...

void setup() {
    // zde vlozte kod, ktery ma bezet pouze jednou

}

void loop() {
    // zde vlozte kod hlavni kod, ktery se bude opakovat donekonecna

}
```

## Blikání LEDkou na desce Arduina
Přímo na desce Arduina je jedna LED, kteoru můžeme z programu ovládat. Je připojena na pin 13. Co budeme potřebovat?

Touto funkcí nastavíme pin 13, kde je připojena LEDka, jako výstup.
```c
pinMode(13, OUTPUT);
```

Touto funkcí přivedeme na pin 13 logickou jedničku (HIGH). Tím se na pin připojí 5V a LEDka se rozsvítí.
```c
digitalWrite(13, HIGH); //zapnutí led
```

Protože mikroprocesor v Arduinu pracuje s frekvencí 16MHz, tak pokud bychom jen neustále měnili stav na pinu, nebylo by blikání pro lidské oko viditelné (viděli bychom jej jen na osciloskopu). Proto přidáme "pauzu", aby oko stihlo vnímat, že LEDka svítí.
```c
delay(1000); // čekání po dobu jedné sekundy
```

Celý program blikání LEDkou:

```c
//sem prijde vlozeni knihoven, inicializace proměnných...
int led = 13;

void setup() {
    // zde vlozte kod, ktery ma bezet pouze jednou
    pinMode(led, OUTPUT);
}

void loop() {
    // zde vlozte kod hlavni kod, ktery se bude opakovat donekonecna
    digitalWrite(led, HIGH); //zapnutí led
    delay(1000); // čekání po dobu jedné sekundy

    digitalWrite(led, LOW); // vypnuti LED
    delay(1000); // čekání po dobu jedné sekundy
}
```

## Přidání další LEDky, nepájivé pole
Na desce Arduina je jen jedna LEDka, kterou můžeme ovládat (pokud nepočítáme LEDky na pinech Tx a Rx, které ale využíváme k programování Arduina). Zkusíme si teď připojit další LEDku s pomocí nepájivého pole. Nesmíme zapomenout na sériový odpor. Jak spočítat jeho velikost?

![image](../img/01_Uvod_LED_4.png)

Nepájivé pole (breadboard) je nástroj, který slouží k rychlému sestavení elektronických obvodů bez nutnosti pájení. Má řadu malých děr, které jsou elektricky propojené, a do těchto děr se zasouvají součástky nebo vodiče. Umožňuje tedy snadno testovat a upravovat obvody.

![image](../img/01_Uvod_LED_5.png)

![image](../img/01_Uvod_LED_6.png)




## Úkoly
**1.** Zapojte do nepájivého pole LEDku s rezistorem. Připojte anodu LEDky na některý digitální pin Arduina (vyberte jeden z pinů 2-12). Napište program tak, aby se vždy po 1s střídavě rozsvěcovala LEDka na Arduino desce (na pinu 13) a LEDka na nepájivém poli.

**2.** Program z předchozího bodu si uložte a vytvořte nový sketch (program). Připojte na jeden pin Arduina tlačítko a na jiný pin LEDku (nezapomeňte na rezistor). Pomocí funkce ```digitalRead()``` čtěte stav tlačítka. Pokud je stisknuté, rozsviťte LEDku. Pokud není stisknuté, LEDku zhasněte. Pin s tlačítkem  nastavte funkcí ```pinMode``` jako ```INPUT_PULLUP```.

**3.** Program z předchozího bodu si uložte a vytvořte nový sketch (program). Vytvořte semafor pomocí Arduina a 3 LED (zelená, žlutá, červená). Vyberte si tři piny Arduina, připojte na každý pin jednu LEDku. Pak naprogramujte pomocí funkcí ```digitalWrite()``` a ```delay()``` aby se stav LEDek měnil podle fází semaforu viz obrázek níže.

![image](../img/01_Uvod_LED_7.png)

**4.** Přidejte k semaforu tlačítko pro chodce (pro auta svítí stále zelená, po stiknutí tlačítka se provede jeden cyklus semaforu, aby stihli chodci přejít a pak opět bude stále svítit zelená, až do dalšího stisknutí).


### [Zpět na obsah](../README.md)
