# Ultrazvukový sensor HC-SR04

![image](https://github.com/user-attachments/assets/b9491ccf-c2ee-4d43-abfb-c589ddbb5567)

*Zdroj obrázku: https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/*

![image](https://github.com/user-attachments/assets/97bf9bf2-9d66-4816-bda1-f13b5380f0e9)

![image](https://lastminuteengineers.com/wp-content/uploads/arduino/HC-SR04-Ultrasonic-Sensor-Working-Echo-reflected-from-Obstacle.gif)

*Zdroj obrázků: https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial/*

## Funkce pulseIn()

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
# Krokový motor

![image](https://github.com/user-attachments/assets/236626cf-0e17-4728-8f1b-6cb44cc3b303)
*Zdroj obrázků: https://playwithcircuit.com/28byj48-stepper-motor-arduino-tutorial/*

![image](https://github.com/user-attachments/assets/92a783b5-af06-4c82-855d-a072e3054543)

*Zdroj obrázků: https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/*

![image](https://blog.seeedstudio.com/wp-content/uploads/2019/03/StepperMotorgif.gif)
*Zdroj obrázku: https://www.seeedstudio.com/blog/2019/03/04/driving-a-28byj-48-stepper-motor-with-a-uln2003-driver-board-and-arduino/*

### Driver ULN2003 

![image](https://github.com/user-attachments/assets/ae61c638-8816-4a27-8a5a-bcce41df2f18)

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

# Definice vlastní funkce v jazyce C 

### Funkce bez parametru a návratové hodnoty

```c
void pozdrav(void)
{
    Serial.println("Dobrý den!");
}
```

### Funkce s parametrem

```c
void pozdrav(char jmeno[])
{
    Serial.print("Dobrý den ");
    Serial.print(jmeno[]);
    Serial.println("!");
}
```

### Návratová hodnota funkce

```c
int obsah_obdelniku(int sirka, int vyska)
{
    int vysledek = sirka * vyska;
    return vysledek;
}
```

### Volání funkce

```c
int a = 5;
int b = 10;
int obsah = obsah_obdelniku(a, b)
Serial.println(obsah);
```
