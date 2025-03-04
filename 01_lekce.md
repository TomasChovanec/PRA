# Úvod do Arduina

## Co je to Arduino?
- HW - desky s různými mikrokontrolery - liší se výkonem, počtem pinů, možnostmi WiFi, Bluetooth atd.
- SW - vývojové prostředí Arduino IDE
- knihovny, jak oficiální tak od komunity uživatelů

## Hardware
<img src="https://github.com/user-attachments/assets/67526fb9-81c3-4751-8cc7-a90bdcac962f" width="600"/>

## Senzory -> Program -> Aktuátory
![image](https://github.com/user-attachments/assets/fcd1f49d-0d64-4522-bc9d-b6a09e957146)

## Příklad projektu s Arduinem
<img src="https://github.com/user-attachments/assets/23add251-c948-4f6d-aee2-ac1156b4b2e6" width="600"/>


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

## Blikání LEDkou

Co budeme potřebovat?

Nastavit pin, kde je připojena LEDka jako výstup
```c
pinMode(13, OUTPUT);
```

Rozsvítit LEDku, tím, že na ni připojíme 5V
```c
digitalWrite(13, HIGH); //zapnutí led
```

Počkat nějakou dobu, abychom lidksé oko vidělo, že LEDka svítí
```c
delay(1000); // čekání po dobu jedné sekundy
```

Celá program blikání LEDkou:

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
    delay(1000); // po dobu jedné sekundy

    digitalWrite(led, LOW); // vypnuti LED
    delay(1000); // po dobu jedné sekundy
}
```

 
- [Připojit k Arduinu tlačítko a číst jeho stav pomocí funkce digitalRead](https://www.itnetwork.cz/hardware-pc/arduino/hardware/arduino-hrajeme-si-s-ledkami)
- [Umět spočítat odpor k LEDce](https://www.youtube.com/watch?v=RnpiNT4ecO4&ab_channel=MichalJakubec) a zapojit je k Arduinu pomocí [nepájivého pole](https://www.youtube.com/watch?v=5ejHjH8z1rk&ab_channel=SP%C5%A0aVO%C5%A0P%C5%99%C3%ADbram)


## Úkoly
1. Blikejte s LEDkou na nepájivém poli (nezapomeňte na rezistor!)
2. Připojte tlačítko a LED – LED se rozsvítí po stisknutí tlačítka. 
3. Vytvořte semafor pomocí Arduina a 3 LED
4. Přidejte k semaforu tlačítko pro chodce (stále zelená, po stiknutí tlačítka se provede jeden cyklus semaforu



### [Zpět na obsah](README.md)
