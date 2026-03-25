# Sériová komunikace
Sériová komunikace představuje jeden z nejjednodušších a nejrozšířenějších způsobů, jak Arduino komunikuje s okolním světem. Pomocí rozhraní UART (Universal Asynchronous Receiver-Transmitter) dokáže Arduino vyměňovat data s počítačem, jinými mikrokontroléry, GPS moduly, Bluetooth moduly, senzory a dalšími periferiemi.

## Funkce Serial.available()
Funkce `Serial.available()` slouží ke zjištění, kolik znaků (bajtů) již dorazilo do přijímacího bufferu sériové linky Arduina a čeká na přečtení.

Díky tomu můžeme ověřit, zda jsou data k dispozici, a zabránit pokusu o čtení v okamžiku, kdy ještě nic nepřišlo.

- vrací celé číslo (počet dostupných bajtů)  
- `Serial.available() == 0` → žádná data nejsou k dispozici  
- `Serial.available() > 0` → v bufferu jsou nová data

Tato funkce se obvykle používá v podmínce `if` nebo v cyklu `while`. Samotné čtení dat (např. pomocí `Serial.read()`, `Serial.readString()` nebo `Serial.parseInt()`) by mělo následovat až ve chvíli, kdy `Serial.available()` vrátí nenulovou hodnotu.

## Funkce Serial.readString()
Funkce `Serial.readString()` načte všechna dostupná data ze sériové linky a uloží je jako textový řetězec (`String`).

Hodí se zejména v případech, kdy očekáváme od uživatele textový vstup.

Čtení končí ve chvíli, kdy:
- už nejsou k dispozici žádná další data  
- nebo vyprší nastavený časový limit (timeout)  

### Příklad:
```cpp
String text_vstup;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    text_vstup = Serial.readString();
    Serial.print("Vase zprava: ");
    Serial.println(text_vstup);
  }
}
```
## Úkoly pro funkci Serial.readString()
1. Připojte k Arduinu LCD displej. Napište program tak, abyste dokázali nastavovat text na displeji přes Serial monitor
2. Upravte program tak, abyste dokázali nastavit text na 1. i druhém řádku.


## Funkce Serial.parseInt()

Funkce Serial.parseInt() slouží ke čtení celých čísel ze sériové linky.
Postupně čte bajty z bufferu, dokud nenarazí na konec čísla nebo na jiný nečíselný znak (např. mezeru nebo koncový znak
řetězce).

Příklad:

```c
int cislo_vstup;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    cislo_vstup = Serial.parseInt();
    Serial.print("Vlozene cislo: ");
    Serial.println(cislo_vstup);
  }
}
```
## Úkoly pro funkci parseInt()
1. Připojte k Arduinu servo. Napište program tak, aby se úhel serva dal nastavovat z počítače přes Serial monitor. Použijte funkci ```Serial.parseInt()```.
1. Přidejte k předchozímu úkolu kontrolu správnosti vstupu (pokud uživatel zadá např. 10000 nebo -13, vypište na Serial monitor chybovou hlášku).


   

## Sériová komunikace mezi Arduiny
Sériová komunikace znamená, že se data posílají **postupně po jednom bitu**, obvykle po jednom vodiči popř. páru vodičů u diferenciálního signálu.  

<img width="951" height="116" alt="image" src="https://github.com/user-attachments/assets/48397fb3-4c05-475b-b1e6-3587fdd45783" />

Na deskách Arduino je hardwarová sériová linka označena jako:

- **TX** (Transmit) – vysílá data  
- **RX** (Receive) – přijímá data  

Pokud chceme propojit UARTem dvě Arduina, musíme jejich Tx a Rx zapojit "do kříže". Navíc musíme propojit země obou zařízení, obě desky musí mít stejnou referenci napětí.

<img width="501" height="149" alt="image" src="https://github.com/user-attachments/assets/de1e4b71-f2d4-4c01-9767-d040c5c739de" />


## Úkol 
- Připojte k jednomu Arduinu RGB LEDku, ke druhému Arduinu připojte tři potenciometry.
- Obě Arduina propojte přes UART (nezapomeňte správně zapojit Tx-Rx Rx-Tx a spojit země obou Arduin).
- Naprogramujte obě Arduina tak, aby se pomocí potenciometrů na jednom Arduinu nastavovaly barevné složky na RGB LEDce na druhém Arduinu.

 
