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
