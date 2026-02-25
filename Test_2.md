## Zadání – Ovládání závory

Součástky:
- servo  
- tlačítko  
- LEDka 

### Funkce
1. Čekání
   - Servo je v základní poloze (např. 0°) a čeká na stisk tlačítka. (např. ```while(digitalRead(tlacitko)==1){}```)
   - LED slabě svítí pomocí analogWrite() (např. hodnota 40).

1. Otevírání
   - Po stisku tlačítka přes `Serial.print()` odešli text: "OTEVIRAM"
   - servo se rychle otevře (např. na 90°)
   - přes `Serial.print()` odešli text: "CEKAM"
   - čekejte 2 s

1. Výstraha před zavíráním
   - LED 5× blikne (200 ms ON, 500 ms OFF)
   - pro blikání používejte `analogWrite()`:
     - pro rozsvícení např. hodnota 180
     - pro zhasnutí hodnota 0

1. Zavírání
   - přes `Serial.print()` odešli text: "ZAVIRAM"
   - Servo se vrátí do původní polohy rychlostí 5° za 20ms.
   - Program se vrátí do čekacího stavu.
