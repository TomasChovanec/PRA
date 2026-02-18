# Sériová komunikace mezi Arduiny

V této lekci budeme posílat data do Arduina přes Serial monitor a pak i mezi dvěma Arduiny. 

Popis potřebných funkcí najdete [zde](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/cteni-uzivatelskych-vstupu-v-arduinu) 


## Úkoly pro funkci parseInt()
1. Připojte k Arduinu servo. Napiště program tak, aby se úhel serva dal nastavovat z počítače přes serial monitor. Použijte funkci ```Serial.parseInt()```.
1. Přidejte k předchozímu úkolu kontrolu správnosti vstupu (co se stane když uživatel zadá např. 10000 nebo -13)

# Sériová komunikace mezi Arduiny

<img width="501" height="149" alt="image" src="https://github.com/user-attachments/assets/de1e4b71-f2d4-4c01-9767-d040c5c739de" />

<img width="951" height="116" alt="image" src="https://github.com/user-attachments/assets/48397fb3-4c05-475b-b1e6-3587fdd45783" />



## Úkol 
- Připojte k jednomu Arduinu RGB LEDku, ke druhému Arduinu připojte tři potenciometry.
- Obě Arduina propojte přes UART (nezapomeňte správně zapojit Tx-Rx Rx-Tx a spojit země obou Arduin).
- Naprogramujte obě Arduina tak, aby se pomocí potenciometrů na jednom Arduinu nastavovaly barevné složky na RGB LEDce na druhém Arduinu.

 
