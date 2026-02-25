# Od Arduino funkcí k registrům

Arduino není samostatný jazyk, ale v zásadě jen vrstva knihoven napsaných v jazyce C/C++, které ovládají registry mikrokontroleru (např. ATmega 328P nebo 2560). Když zavoláte funkci jako digitalWrite(), uvnitř se stejně nastavují konkrétní bity v registrech jako PORTx, DDRx nebo PINx. Funkce jako millis() nebo delay() jen konfigurují a používají hardwarové časovače přes registry typu TCCR, TCNT a podobně. Rozdíl je jen v tom, že Arduino tyhle operace schová do přehledných funkcí, aby začátečník nemusel řešit datasheet a bitové masky.
Z pohledu principu je to ale úplně stejná práce s registry, jakou se učíte v kurzu MIT – jen zabalená do pohodlnějšího rozhraní.


Přestože v Arduino IDE nevidíme funkci main(), ve skutečnosti tam samozřejmě je. Je definovaná v jádru Arduino frameworku a po resetu mikrokontroléru se spustí úplně stejně jako v projektu vytvořeném v Microchip Studiu. Uvnitř této funkce se nejdřív provede inicializace hardwaru a knihoven a potom se jednou zavolá setup(). Následně běží nekonečná smyčka while(1), ve které se pořád dokola volá loop(). Takže místo abychom psali vlastní while(1), Arduino ji píše za nás – princip běhu programu je ale naprosto stejný.
```c
int main(void)
{
    init();          // inicializace hardware (timery, UART...)
    setup();         // uživatelský setup

    while (1)
    {
        loop();      // uživatelská smyčka
    }
}
```

## Přiřazení pinů Arduina k portům mikrokontroleru
Arduino používá vlastní číslování pinů (0, 1, 2, …), které je jen „uživatelské“ a nemá přímou souvislost s názvy portů v mikrokontroléru. Uvnitř ATmegy jsou ale piny organizované do portů (PORTB, PORTC, PORTD) a každý pin je konkrétní bit v příslušném registru.
Například digitální pin 13 na Arduino UNO je ve skutečnosti bit 5 v registru PORTB, tedy PB5. Když tedy zapíšete do PORTB |= (1<<5);, ovládáte fyzicky stejný vývod jako při použití digitalWrite(13, HIGH);.
Je důležité si uvědomit, že číslo pinu na desce je jen mapování – skutečná práce se vždy děje přes konkrétní port a jeho bit v registrech mikrokontroléru.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/10424de5-d163-49e9-b062-c5cca09aba09" />


## Úkoly

1. Připojte k Arduinu LEDku na libovolný pin. Napište program pro blikání LEDkou (500ms ON, 500ms OFF). Nepoužívejte funkce pinMode() a digitalWrite(), delay() použít můžete. Pro nastavení pinu jako výstupu a ovládání LEDky pracujte přímo s registry mikroprocesoru, stejně jako v předmětu MIT. Viz [lekce MIT](https://tomaschovanec.github.io/MIT/02_Blikani_LED.html)

1. Napište program, který bude co nejrychleji měnit logickou hodnotu na pinu (střídat 1 a 0). Nejprve použijte funkci digitalWrite() a logickým analyzerem změřte periodu a frekvenci signálu. Pak zkuste stejný program napsat bez použití digitalWrite() jen přímou manipulací registrů. Opět změřte výsledný signál a porovnejte obě metody. 

1. Napište program, který bude LEDkou blikat s periodou 200ms bez použití funkce delay(), pouze pomocí časovače Timer1 viz [lekce MIT](https://tomaschovanec.github.io/MIT/08_Timer.html)

