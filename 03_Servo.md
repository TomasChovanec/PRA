# Servomotor

### Cíle lekce
- Pochopit jak funguje modelářské servo, z čeho se skládá, jak se řídí
- Umět přidat do Arduino program knihovnu
- Ovládat servo pomocí knihovny

## Servomotor SG-90
Je to malý motor s převodovkou, který umí přesně natočit hřídel do určitého úhlu (většinou 0–180°).
Uvnitř najdeme:
- DC motor – pohon
- Převodovku – zpomalí a zvýší moment (sílu) serva
- Potenciometr – snímá polohu hřídele
- Deska s řídící elektronikou - řídí motor na základě signálu z řidícího vodiče a potenciometru

![image](img/03_Servo_PWM_1.png)

*Zdroj obrázku: https://docs.arduino.cc/tutorials/generic/basic-servo-control/*

## Zapojení serva

![image](img/03_Servo_PWM_2.png)

*Zdroj obrázku: https://lastminuteengineers.com/servo-motor-arduino-tutorial/*

## Řízení serva
Servo se ovládá pomocí PWM signálu – konkrétně šířkou impulzu.

Perioda trvá 20 ms (50 Hz). Délka impulzu určuje úhel:

0,5 ms → Servo na 0°

1,5 ms → 90° (střed)

2,5 ms → 180°

Arduino knihovna Servo tuto práci zjednodušuje:
servo.attach(pin) — určí, na který pin je servo připojené.
servo.write(úhel) — nastaví úhel (0 až 180°).

![image](https://lastminuteengineers.com/wp-content/uploads/arduino/Servo-Motor-Working-Animation.gif)

*Zdroj obrázku: https://lastminuteengineers.com/servo-motor-arduino-tutorial/*

<img src="img/03_Servo_PWM_3.png" width="800"/>

*Zdroj obrázku: https://howtomechatronics.com/how-it-works/how-servo-motors-work-how-to-control-servos-using-arduino/*


## Program pro servo

```c
#include <Servo.h>  // Přidáme knihovnu Servo

Servo servo1; // Vytvoříme si objekt serva

void setup() {

  servo1.attach(2);  // Nastavíme číslo pinu, kde je servo připojeno

}

void loop() {

    servo1.write(0); // Nastaví servo do polohy 0°
    delay(500);     // Počkáme dostatečně dlouho, než servo dosáhne požadované pozice                 

    servo1.write(90);  // Nastaví servo do polohy 90°    
    delay(500);        // Počkáme dostatečně dlouho, než servo dosáhne požadované pozice            

}
```

### Úkoly:
1. Připojte k Arduinu servo, použijte program z příkladu výše a zkuste upravovat časy a úhly.
2. Vytvořit program, který bude servem pohybovat od 0°do 180° plynule (změní úhel vždy jen o jeden stupeň)
3. Připojte k Arduinu servo a potenciometr. Polohu serva nastavujte pomocí potenciometru. Můžete pro to použít funkci map() kterou najdete níže.


## Funkce map()
Funkce map() v Arduinu slouží k převedení hodnoty z jednoho rozsahu do druhého. To je užitečné, když máme třeba hodnotu z analogového vstupu (0 až 1023) a chceme ji převést na jiný rozsah, třeba pro servo (0 až 180 stupňů) nebo pro jas LEDky (0 až 255).

Použití funkce:

```long map(long value, long fromLow, long fromHigh, long toLow, long toHigh);```

```value```: vstupní hodnota, kterou chceme převést

```fromLow```, ```fromHigh```: původní rozsah hodnot

```toLow```, ```toHigh```: nový rozsah hodnot

Příklad použití:
```c
int potValue = analogRead(A0);  
int angle = map(potValue, 0, 1023, 0, 180);  
servo.write(angle);
```

analogRead() vrátí hodnotu od 0 do 1023
map() ji převede na úhel od 0 do 180 stupňů pro servo

## [Zpět na obsah](README.md)
