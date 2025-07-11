# Ultrazvukový sensor HC-SR04
V dnešní lekci se naučíme pracovat se senzorem HC-SR04, který umožňuje měření vzdálenosti pomocí ultrazvuku. 

Hlavní parametry senzoru:

| Parametr              | Hodnota           |
|-----------------------|------------------|
| Napájecí napětí       | 5V               |
| Proudový odběr   | ~15 mA           |
| Frekvence ultrazvuku | 40 kHz       |
| Měřicí rozsah    | 2 – 400 cm       |
| Přesnost         | ±3 mm            |
| Úhel detekce     | ~15°             |
| Rozhraní         | 2 digitální piny (Trig, Echo) |

## Princip senzoru

![image](img/05_Ultrasonic_stepper_1.png)

*Zdroj obrázku: https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/*

### Zapojení
Kromě obligátního +5V napájení a GND musíme čidlo připojit ke dvěma libovolným digitálním pinům Arduina. **Pin Trig** slouží ke spuštění měření (vyslání ultrazvukového pulzu), musíme jej tedy v Arduinu nastavit jako výstup. **Pin Echo** je výstup senzoru (tedy z pohledu Arduina vstup), na kterém senzor generuje puls, jehož délka odpovídá době od vyslání signálu do návratu odražené vlny.

![image](img/05_Ultrasonic_stepper_2.png)

![image](https://lastminuteengineers.com/wp-content/uploads/arduino/HC-SR04-Ultrasonic-Sensor-Working-Echo-reflected-from-Obstacle.gif)

*Zdroj obrázků: https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/*

### Funkce pulseIn()
Abychom zjistili změřenou vzdálenost, potřebujeme změřit délku pulzu na pinu Echo. Mohli bychom pro to použít periferii mikrokontroleru časovač, ale usnadníme si práci využitím standartní funkce Arduino pulseIn(). Funkce vyžaduje dva argumenty -  na jakém pinu chceme pulz měřit a zda chceme měřit délku HIGH nebo LOW pulzu.

```c
int pin = 7;
unsigned long duration;

void setup() {
  Serial.begin(9600);
  pinMode(pin, INPUT);
}

void loop() {
  duration = pulseIn(pin, HIGH);
  Serial.println(duration);
}
```

### Úkoly
1. Připojte k Arduinu ultrazvukový senzor. Měřte vzdálenost a změřenou hodnotu posílejte na serial monitor.
2. Přidejte navíc LCD displej a naměřenou hodnotu na něm zobrazujte v centimetrech. Připojte Arduino na powerbanku a zkuste změřit i větší vzdálenosti v místnosti. Ověřte limity senzoru.


# Krokový motor
Dalším zařízení, které si zkusíme řídit Arduinem bude krokový motor. V našem případě malý unipolární krokový motor **28BYJ-48**.

### Schema zapojení, princip funkce
Motor 28BYJ-48 je unipolární krokový motor se čtyřmi cívkami uspořádanými do dvou sekcí. Každá sekce má střední odbočku připojenou na 5V. Když připojíme jeden z konců cívky k zemi, začne cívkou procházet proud, což vytvoří magnetické pole. Interakce tohoto pole s magnetickým polem permanentního magnetu v rotoru způsobí pootočení motoru o jeden krok. Postupným přepínáním napájení mezi jednotlivými cívkami dochází k rotaci motoru krok za krokem

![image](img/05_Ultrasonic_stepper_3.png)

*Zdroj obrázků: https://playwithcircuit.com/28byj48-stepper-motor-arduino-tutorial/*

![image](https://blog.seeedstudio.com/wp-content/uploads/2019/03/StepperMotorgif.gif)

*Zdroj obrázku: https://www.seeedstudio.com/blog/2019/03/04/driving-a-28byj-48-stepper-motor-with-a-uln2003-driver-board-and-arduino/*

### Převodovka
Pro dosažení vyššího momentu a jemnějšího řízení polohy je motor vybaven převodovkou s přibližným převodovým poměrem1:64, tedy pro jedno plné otočení výstuponí hřídele je potřeba přibližně 64 otáček motoru.

![image](img/05_Ultrasonic_stepper_4.png)

*Zdroj obrázků: https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/*

## Driver ULN2003 
Protože motorem teče příliš velký proud na to, abychom ho řídilo piny Arduina napřímo, použijeme driver pro krokový motor. Ten nám poslouží jako výkonový spínač.

![image](img/05_Ultrasonic_stepper_5.png)

*Zdroj obrázků: https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/*

```c
#include <Stepper.h>

//define Input pins of the Motor
#define OUTPUT1   7                // Connected to the Blue coloured wire
#define OUTPUT2   6                // Connected to the Pink coloured wire
#define OUTPUT3   5                // Connected to the Yellow coloured wire
#define OUTPUT4   4                // Connected to the Orange coloured wire

// Define the number of steps per rotation
const int stepsPerRotation = 2048;  // 28BYJ-48 has 2048 steps per rotation in full step mode as given in data sheet

// Initialize the stepper motor with the sequence of control pins OUTPUT1, OUTPUT3, OUTPUT2, IN4
// OUTPUT1 and OUTPUT3 are connected to one coil and OUTPUT2 and OUTPUT4 are connected to one Coil
Stepper myStepper(stepsPerRotation, OUTPUT1, OUTPUT3, OUTPUT2, OUTPUT4);  
void setup() {
  // Set the speed of the motor in RPM (adjust as needed)
  myStepper.setSpeed(15);  // 15 RPM
}

void loop() {
  // Rotate in One Direction and complete one complete rotation i.e 2048 steps
  myStepper.step(stepsPerRotation);  
  delay(1000);  // Delay between rotations
  // For Rotation in opposite direction provide the variable to the parameter with negative Sign
  myStepper.step(-stepsPerRotation);  
  delay(1000);  // Delay between rotations
}
```

### Úkoly
1. Připojte k Arduinu krokový motor a otáčejte čtvrt otáčky doleva a půl otáčky doprava.
2. Přidejte ještě tlačítko. Při držení tlačítka se bude motor točit doleva, pokud tlačítko není stisknuto tak doprava.



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
1. Vytvořte funkci pro blikání LEDkou ```blikej(int pocet_bliknuti, int delka_bliknuti);```
2. Pro snadnější práci s ultrazvukovým senzorem vytvořte funkci ```zmer_vzdalenost()```, která bude vracet délku v centimetrech.
3. Vytvořte program, který umožní uživateli nejprve změřit šířku místnosti, pak délku a následně zobrazí plochu místnosti.
4. Vytvořte funkci, která pootočí krokovým motorem o čtyři kroky (postupným sepnutím všech čtyř cívek). Nepoužívejne žádnou knihovnu, cívky motoru spínejte pomocí funkce ```digitalWrite()```.
5. Upravte funkci z předchozího bodu tak, aby jako vstupní argument přijímala počet počet kroků motoru.

## [Zpět na obsah](README.md)
