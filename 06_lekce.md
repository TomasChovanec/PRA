## Stejnosměrný motor
DC motor (stejnosměrný motor) je zařízení, které převádí elektrickou energii na mechanickou – konkrétně na otáčivý pohyb. Komutátor při otáčení motoru přepíná směr proudu, takže se motor točí stále stejným směrem.

**Stator** – pevná část, vytváří stálé magnetické pole (např. pomocí permanentních magnetů).

**Rotor (kotva)** – točivá část, obsahuje vinutí (cívky), do kterých se přivádí proud.

**Komutátor** – mechanický přepínač, který přepíná směr proudu ve vinutí během otáčení.

**Kartáče (uhlíky)** – přivádějí proud do komutátoru.

Video [o konstrukci stejnosměrného motoru](https://youtu.be/LAtPHANEfQo?feature=shared)

<img src="https://github.com/user-attachments/assets/3ea712a0-9cc0-4406-ba1f-e87f0a42a647" width="450"/>

*Zdroj obrázku: https://dronebotworkshop.com/dc-motors-l298n-h-bridge/*

## H-můstek
H-můstek (anglicky H-bridge) je elektronický obvod, který slouží k řízení směru otáčení DC motoru. Umožňuje motor otáčet na jednu stranu,na druhou stranu nebo zastavit (volitelně i regulovat rychlost pomocí PWM).
Obsahuje 4 spínače (např. tranzistory) uspořádané do tvaru písmene H. Přepínáním těchto spínačů lze změnit směr proudu procházejícího motorem a tím směr otáčení.

[H-můstku](https://www.circuitbread.com/ee-faq/how-does-an-h-bridge-work)

<img src="https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/h-bridge-circuit-600w.gif" width="450"/>

Pro řízení rychlosti DC motoru můžeme použít PWM pomocí funkce analogWrite().

<img src="https://github.com/user-attachments/assets/4adedba1-d284-4885-8916-f354b1a89779" width="450"/>


## Výukový robot
<img src="https://github.com/user-attachments/assets/121c0a41-5f67-464c-952a-cd94e64ed80b" width="450"/>

Robot, kterého budeme ve výuce použivat, v sobě obsahuje Arduino Nano (má stejný procesor jako Arduino UNO, které obvykle používáme, ale má menší desku). Aby mohl jezdit, má dva stejnosměrné motory s převodovkou, kteér jsou řízeny pomocí H můstku DRV8833. [Schéma](https://github.com/TomasChovanec/Arduino_robotek/blob/master/FrenGP_robot/Robot_schematics.pdf) pro výukového robota ke stažení [zde](https://github.com/TomasChovanec/Arduino_robotek/raw/master/FrenGP_robot/Robot_schematics.pdf)

## Pinout modulu DRV8833 a princip použití
Obvod [DRV8833](https://lastminuteengineers.com/drv8833-arduino-tutorial/) v sobě obsahuje dva H můstky, můžeme s ním tedy řídít dva stejnosměrné motory. Vstupy IN1-4 připojíme k pinům Arduina, které podporují PWM výstup, abychom mohli řídit plynule rychlost motorů.

![image](https://github.com/user-attachments/assets/da091db0-988e-4b6a-8ebb-67f0800a81e2)

![image](https://github.com/user-attachments/assets/f02e396e-7b49-419c-a0f7-dc624c312414)


## Režimy ovládání motoru
Zda a jakým směrem se motory budou točit nastavíme kombinací vstupů IN1 a IN2 pro první motor a IN3 A IN4 pro druhý motor:

![image](https://github.com/user-attachments/assets/09f7810d-7b68-41ac-b7b3-3359092e08af)

## Úkoly
1. Prostudujte si schéma robota. Zkuste roztočit oba motory.
2. Vytvořte funkce ```vpred(int rychlost)```, ```vzad(int rychlost)```, ```vlevo(int rychlost)```, ```vpravo(int rychlost)``` a ```stop()```
3. Napište program, kde robot jede vpřed 2 sekundy, pak se otočí doprava a jede dál.
4. Robot pojede dopředu, po 3s se otočí o 180°a pojede zpět.
5. Přidejte bezpečnostní funkci - robot se spustí až po stisknutí tlačítka.
6. Použijte ultrazvukový senzor pro detekci překážky - pokud je detekována překážka do 20 cm, zastavte robota.
7. Stejně jako v předchozím bodě, ale přidejte při detekci překážky automatické couvání a otočení.


## [Zpět na obsah](README.md)
