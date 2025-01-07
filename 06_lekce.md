
## Vlastní funkce v jazyce C
- Zopakujeme si princip funkcí v jazyce C, co je návratová hodnota, argument, jak se funkce volá
  
- Zkusíme si nadefinovat [vlastní funkci](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/funkce-a-knihovny)

## Stejnosměrný motor
- Ukážeme si princip funkce [stejnosměrného motoru](https://youtu.be/LAtPHANEfQo?feature=shared)

<img src="https://github.com/user-attachments/assets/3ea712a0-9cc0-4406-ba1f-e87f0a42a647" width="450"/>

*Zdroj obrázku: https://dronebotworkshop.com/dc-motors-l298n-h-bridge/*

## H-můstek
- Projdeme si princip řízení směru otáčení motoru pomocí [H-můstku](https://www.circuitbread.com/ee-faq/how-does-an-h-bridge-work)

<img src="https://cdn.sparkfun.com/assets/learn_tutorials/1/9/3/h-bridge-circuit-600w.gif" width="450"/>

- Použijeme funkci analogWrite pro řízení rychlosti DC motoru

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

