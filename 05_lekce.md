# Ultrazvukový sensor HC-SR04

![image](https://github.com/user-attachments/assets/b9491ccf-c2ee-4d43-abfb-c589ddbb5567)

![image](https://github.com/user-attachments/assets/97bf9bf2-9d66-4816-bda1-f13b5380f0e9)

![image](https://lastminuteengineers.com/wp-content/uploads/arduino/HC-SR04-Ultrasonic-Sensor-Working-Echo-reflected-from-Obstacle.gif)

![image](https://github.com/user-attachments/assets/999d9d9c-e60e-4769-892b-5b77e7c7be82)


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


![image](https://github.com/user-attachments/assets/0bf31bf3-3fa2-4b1c-a9af-a77890bed561)

![image](https://github.com/user-attachments/assets/5d9f0b83-d1fb-4aac-9db3-7c90850fc972)

![image](https://github.com/user-attachments/assets/ae61c638-8816-4a27-8a5a-bcce41df2f18)

*Zdroj obrázku: https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/*

![image](https://github.com/user-attachments/assets/3a35d953-4fe2-48ca-ba4c-d6140944218b)

*Zdroj obrázku: https://playwithcircuit.com/28byj48-stepper-motor-arduino-tutorial/*

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

- Chápat princip funkce [krokového motoru](https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/)
- Umět použít krokový motor se základní [knihovnou Stepper.](https://www.instructables.com/How-to-Control-28BYJ-48-Stepper-Motor-With-ULN2003/)
- 
# Definice vlastní funkce v jazyce C 

### FUnkce bez parametru a návratové hodnoty

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
