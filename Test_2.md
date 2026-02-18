## Zadání – Ovládání závory

Součástky:
- servo  
- tlačítko  
- červená LED  

### Funkce
1. Čekání
   - Servo je v základní poloze (např. 0°) a čeká na stisk tlačítka. (např. ```while(digitalRead(tlacitko)==1){}```)

1. Otevírání
   - Po stisku tlačítka přes `Serial.print()` odešli text: "OTEVIRAM"
   - servo se rychle otevře (např. na 90°)
   - přes `Serial.print()` odešli text: "CEKAM"
   - čekej 3 s

1. Výstraha před zavíráním
   - LED 4× blikne (300 ms ON, 700 ms OFF)
   - během blikání používej `analogWrite()`:
     - pro rozsvícení např. hodnota 180
     - pro zhasnutí hodnota 0

1. Zavírání
   - přes `Serial.print()` odešli text: "ZAVIRAM"
   - Servo se pomalu po malých krocích (např. 1° za 10ms) vrátí do původní polohy.
   - Program se vrátí do čekacího stavu.
