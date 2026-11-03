# Logický analyzer

## Cíle lekce
- Porozumět základnímu principu logického analyzátoru.
- Naučit se zachytit a analyzovat PWM signál.
- Umět dekódovat UART komunikaci.
- Umět dekódovat I2C komunikaci.

## Co je logický analyzátor

<img width="1113" height="523" alt="image" src="https://github.com/user-attachments/assets/3a340a0b-d616-441f-9e0c-c7794c35d54c" />

Logický analyzátor je nástroj pro zachytávání digitálních signálů. 
Umožňuje:
- měřit více kanálů současně (zde 8 kanálů),
- zaznamenat jejich průběh v čase,
- zobrazit změny stavu (LOW/HIGH),
- měřit časové intervaly
- automaticky dekódovat protokoly (UART, I2C, SPI atd.).

Typický analyzátor pracuje s napěťovou úrovní 0–5 V.

### Pokus s logickým analyzerem
- připojte k Arduinu LEDku na pin 9 a do arduina naflashujte kód níže
- připojte libovolné kanály logického analyzéru na
    - Pin 13 Arduina
    - Pin 9 Arduina
    - Pin 1 (Tx) Arduina
    - Propojte zem analyzeru se zemí Arduina
- spusťte program Logic a sledujte průběhy napětí na jednotlivých kanálech 


```c
void setup() {
  pinMode(9, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // LED na PWM pinu - zesilování a zeslabování
  for (int i = 0; i <= 255; i += 5) {
    analogWrite(9, i);
    delay(30);
  }

  for (int i = 255; i >= 0; i -= 5) {
    analogWrite(9, i);
    delay(30);
  }

  // LED na pinu 13 - blikání
  digitalWrite(13, HIGH);
  Serial.println("LED1: 80%. LED2: ON");
  delay(500);

  digitalWrite(13, LOW);
  Serial.println("LED1: 80%. LED2: OFF");
  delay(500);
}

```
