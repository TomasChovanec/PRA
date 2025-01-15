# Časování s funkcí millis()

## Problémy s funkcí delay()
Když jsme doteď chtěli nastavit v programu nějaké časování (např blikat LEDkou jednou za sekundu), používali jsme funkci delay(). Výhoda této funkce je, že je jednoduchá a snadno se používá. Ale nevýhodou je, že během čekání ve funkci dleay() nemůže procesor dělat nic jiného. Pokud děláme jednoduchý program, který dělá jen jednu věc, tak nám to nevadí.

Např. pokud chceme blikat  LEDkou jednou za sekundu , není to problém:

```c
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
```

Co ale když budeme k příkladu výše chtít přidat druhou LEDku a tou blikat 10x za sekundu? Nebo číst stav tlačítka každých 200ms? Nebo posílat data na displej každých 100ms? Nic z toho dělat nemůžeme, protže během vykonávání funkce delay() procesor nic jiného nedělá, jen čeká.

**Úkol:** Vytvořte program, který bliká LEDkou jednou za sekundu pomocí funkce delay. Pak program rozšiřte tak, aby se při stisknutí tlačítka rozsvítila jiná LEDka. Funguje program vždy správně? Reaguje na tlačítko vždy okamžitě? 


## Funkce millis()

Funkci delay() chceme tedy v našich programech používat pokud možno minimálně. Jak ale jinak zajistit, aby se příkazy vykonávaly s časováním, jaké chceme? Můžeme použít funkci millis(). Funkce millis() nám vrací počet milisekung od startu programu. Nemusíte ji nijak spouštět nebo inicializovat, využívá na pozadí časovač, který se spustí automaticky po každém resetu.

**Úkol:** Posílejte pomocí funkce Serial.println() výsledek funkce millis na sériový monitor. Sledujte, co se stane, když resetujete Arduino reset tlačítkem.

Poznámka: Funkce millis vrací výsledek jako datový typ **unsigned long**, pokud její výsledek chcete uložit do proměnné, použijte tento datový typ. K přetečení časovače dojde přibližně jednou za 50 dní. (4 294 967 295 ms = 4 294 967 s = 71 582 min = 1193 h = 49,7 dní)

**Úkol:** Využijte funkci millis() k tomu, abyste vždy 2 sekundy po resetu procesoru rozsvítili LEDku

V předchozím úkolu jsme použili podmínku if a porovnávali jsme aktuální výsledek funkce millis s nějakou konstantou. Co když ale chceme, ale se LEDka nerozsvítila jen jednou, ale aby změnila svůj stav každé 2 sekundy? Můžeme si uložit aktuální stav funkce millis do proměnné a pak vždy porovnávat aktuální čas s tím uloženým. Pokud se budou lišit o 2000ms, tak změníme stav LEDky a zase si uložíme do proměnné čas posledního bliknutí.

<img src="https://i0.wp.com/www.programmingelectronics.com/wp-content/uploads/2019/04/Arduino-timeline-gif-2.gif" width="400"/>

*Zdroj obrázku: https://www.programmingelectronics.com/arduino-sketch-with-millis-instead-of-delay/*


```c
const int ledPin = 12; 

int ledState = LOW; // proměnná s uloženým posledním stavem LEDky
unsigned long previousMillis = 0;  // čas, kdy jsme naposledy bliknuli LEDkou

int interval = 2000;  // interval ve kterém chceme LEDkou blikat (v milisekundách)

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis > interval) {
    // uložíme čas, kdy jsme naposledy bliknuli LEDkou
    previousMillis = currentMillis;

    // pokud je LEDka zhasnutá, rozsvítíme ji a naopak
    if (ledState == LOW) {
      ledState = HIGH;
    } 
    else {
      ledState = LOW;
    }
    // nastavíme požadovaný stav LEDky
    digitalWrite(ledPin, ledState);
  }
}
```

Nyní můžeme zkusit stejný úkol jako na začátku, ale namísto delay() použít millis(). Díky tomu už náš program nebude trpět zpožděnou reakcí na tlačítko.

**Úkol:** Vytvořte program, který bliká LEDkou jednou za sekundu pomocí funkce millis(). Pak program rozšiřte tak, aby se při stisknutí tlačítka rozsvítila jiná LEDka. 


## Další užitečné články a videa

[Video k funkci millis()](https://www.youtube.com/watch?v=BYKQ9rk0FEQ&ab_channel=ProgrammingElectronicsAcademy)

[Tutorial k millis()](https://bastlirna.hwkitchen.cz/arduino-zaklady-blikani-bez-funkce-delay/)


### [Zpět na obsah](README.md)
