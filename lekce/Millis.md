# Multitasking (neblokující kód) s Arduinem

## Cíl lekce
- pochopit, proč používání `delay()` způsobuje problémy
- naučit se používat funkci `millis()`  
- zvládnout s Arduinem řídit více věcí „současně“
  
## Problém s `delay()`

Doteď jsme pro časování používali funkci `delay()`:

    digitalWrite(13, HIGH);
    delay(2000);
    digitalWrite(13, LOW);
    delay(2000);

Funguje to, ale má to zásadní nevýhodu: Během `delay()` procesor nic jiného nedělá.

## Úkol 1

Připojte k Arduinu 2 LEDky a tlačítko. Vytvořte program:
- LED1 bliká (2 s zapnuto, 2 s vypnuto)
- tlačítko rozsvítí LED2 (svítí jen při stisku)

### Otázky
- Reaguje LED2 vždy okamžitě?
- Co se stane při krátkém stisku tlačítka?


## Jak to řešit jinak?

Místo čekání použijeme jiný přístup:

> Nebudeme čekat, ale budeme se ptát: „Už uběhl potřebný čas?“


## Funkce `millis()`

Funkce `millis()` vrací počet milisekund od startu programu.

> Představte si, že máte stopky, které běží nepřetržitě od chvíle, kdy jste Arudino zapnuli. Funkcí millis() se jednoduše zeptáme: 'Kolik milisekund na těch stopkách právě je?' — a okamžitě dostaneme odpověď. Nic to nepozastaví, nic neblokuje.


## Úkol 2

Vypisujte hodnotu `millis()` na sériový monitor:
    unsigned long cas = millis();
    Serial.println(cas);

### Sledujte
- Co se stane po resetu Arduina?

## Úkol 3

Rozsviťte LED po 2 sekundách od startu programu.

## Základní princip

Nejdůležitější myšlenka:

> Porovnáváme rozdíl časů, ne konkrétní hodnotu.

    if (currentMillis - previousMillis > interval)

<img src="https://i0.wp.com/www.programmingelectronics.com/wp-content/uploads/2019/04/Arduino-timeline-gif-2.gif" width="400"/>

*Zdroj obrázku: https://www.programmingelectronics.com/arduino-sketch-with-millis-instead-of-delay/*

## Více úloh současně

## Úkol 4

Vytvořte program:
- LED1 bliká každé 2 sekundy  
- LED2 bliká každých 200 ms  
- tlačítko rozsvítí LED3 okamžitě při stisku  

### Nápověda
Každá úloha potřebuje:
- vlastní interval  
- vlastní čas poslední změny  
- vlastní stav  

### Příklad struktury

    // LED1
    if (...) {
      ...
    }

    // LED2
    if (...) {
      ...
    }

    // tlačítko
    if (...) {
      ...
    }


## Shrnutí

- `delay()` blokuje program  
- `millis()` umožňuje neblokující časování  
- klíč je porovnání rozdílu časů  

    currentMillis - previousMillis

> Arduino neumí skutečný multitasking, ale můžeme ho napodobit.

## Další užitečné články a videa

[Video k funkci millis()](https://www.youtube.com/watch?v=BYKQ9rk0FEQ&ab_channel=ProgrammingElectronicsAcademy)


### [Zpět na obsah](../README.md)
