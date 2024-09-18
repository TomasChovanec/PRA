```c
#include <Servo.h>  //pridame knihovnu Servo

Servo servo1; // vytvorime si objekt serva

void setup() {

  servo1.attach(2);  // nastavime cislo pinu, kde je servo pripojeno

}

void loop() {

    servo1.write(0); //nastavi servo do polohy 0°
    delay(500);     //pockame dostatecne dlouho, nez servo dosahne pozadovane pozice                 

    servo1.write(90);  //nastavi servo do polohy 90°    
    delay(500);        //pockame dostatecne dlouho, nez servo dosahne pozadovane pozice            

}

```
