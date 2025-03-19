# Opakování z minula

**Úkol:** Čtení hodnoty z potenciometru a výstup na sériový port
- Připojte potenciometr k Arduinu (střední pin potenciometru na analogový vstup, krajní piny na VCC a GND).  
- Číslo pinu potenciometru uložte do **proměnné**, abyste ho mohli později snadno změnit.  
- Přečtěte aktuální hodnotu potenciometru a **uložte ji do proměnné**.  
- Na sériový port pravidelně vypisujte zprávu ve formátu: "Hodnota je: xx." (místo `xx` bude aktuální hodnota potenciometru). 
- Pokud hodnota potenciometru přesáhne **800**, vypište navíc zprávu: "Varování, vysoká hodnota!


# Servomotor

![image](https://github.com/user-attachments/assets/5848885d-49c4-4c21-ab24-8e94c17b9db6)

*Zdroj obrázku: https://docs.arduino.cc/tutorials/generic/basic-servo-control/*

## Ovládání serva

![image](https://lastminuteengineers.com/wp-content/uploads/arduino/Servo-Motor-Working-Animation.gif)

*Zdroj obrázku: https://lastminuteengineers.com/servo-motor-arduino-tutorial/*

<img src="https://github.com/user-attachments/assets/679321bf-ee7d-42cc-9ea8-ecc5c2172239" width="800"/>

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
    delay(500);     //pockame dostatecne dlouho, nez servo dosahne pozadovane pozice                 

    servo1.write(90);  // Nastaví servo do polohy 90°    
    delay(500);        // Počkáme dostatečně dlouho, než servo dosáhne požadované pozice            

}
```

## Úkoly:
1. Připojte k Arduinu servo, použijte program z příkladu výše a zkuste upravovat časy a úhly.
2. Vytvořit program, který bude servem pohybovat od 0°do 180° plynule (změní úhel vždy jen o jeden stupeň)
3. Připojte k Arduinu servoa potenciometr. Polohu serva nastavujte pomocí potenciometru. Můžete pro to použít funkci map() kterou najdete níže.


## Funkce map()
Funkce map() v Arduinu slouží k převedení hodnoty z jednoho rozsahu do druhého. To je užitečné, když máme třeba hodnotu z analogového vstupu (0 až 1023) a chceme ji převést na jiný rozsah, třeba pro servo (0 až 180 stupňů) nebo pro jas LEDky (0 až 255).

long map(long value, long fromLow, long fromHigh, long toLow, long toHigh);
**value**: vstupní hodnota, kterou chceme převést
**fromLow**, **fromHigh**: původní rozsah hodnot
**toLow**, **toHigh**: nový rozsah hodnot

Příklad použití:
```C
int potValue = analogRead(A0);  
int angle = map(potValue, 0, 1023, 0, 180);  
servo.write(angle);
```

analogRead() vrátí hodnotu od 0 do 1023
map() ji převede na úhel od 0 do 180 stupňů pro servo

## PWM s Arduinem - funkce analogWrite()
PWM regulaci znáte z jiných předmětů. Ve zkratce, je to způsob, jak měnit efektivní hodnotu napětí pomocí periodického zapínání a vypínání. Čím vyšší část doby je signál v logické 1, tím je efektivní hodnota vyšší. PWM můžeme použít například při regulaci motorů, tepelných spotřebičů nebo zdrojů světla.

V Arduinu můžeme PWM snadno nastavovat pomocí funkce analogWrite(). 

Zápis: ```analogWrite(pin, hodnota);```

Hodnota je od 0 (0%) do 255 (100%).

:warning:Funkce analogWrite je dostupná pouze pro některé piny. Ty jsou označené na desce znakem vlnovky.


## RGB LED


![image](https://github.com/user-attachments/assets/465749f3-a24b-405c-ab2b-98ac3fbccb0c)

*Zdroj obrázku: https://www.build-electronic-circuits.com/rgb-led/*

![image](https://github.com/user-attachments/assets/b545e2e4-bc11-4919-a790-c9a725298bcb)

*Zdroj obrázku: https://howtomechatronics.com/tutorials/arduino/how-to-use-a-rgb-led-with-arduino/*



## [Zpět na obsah](README.md)
