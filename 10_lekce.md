# 10 - Bluetooth

V dnešní lekci si ukážeme jak použít s Arduinem bezdrátovou komunikaci. Asi nejsnazší cestou je technologie Bluetooth. Je to 2,4GHz rádiový přenos určený na krátké vzdálenosti, který běžně používáme k připojení bezdrátových periferií jako sluchátek, reproduktorů, myší, klávesnic a mnoha dalšího. Dále můžeme s jeho pomocí například sbírat data ze senzorů nebo ovládat různá zařízení přes aplikaci na telefonu.

## HC-05
V této lekci budeme používat bluetooth modul HC-05, který je velmi rozšířený, pro svou nízkou cenu a jednoduchou obsluhu. Nevýhoda je, že podporuje pouze starší standard Bluetooth 2.0, a proto není kompatibilní s výrobky firmy Apple. Ovšem lze ho použít ke komunikaci s telefony Android, s notebooky či nevázat komunikaci mezi dvěma moduly HC-05.

## Použití
HC-05 funguje jako bezdrátový UART bridge. Tedy pokud ho připojíme k pinům Rx a Tx Arduina, všechna data, která prostřednictvím sériové linky pošleme, se přenesou bezdrátově do spárovaného zařízení (mobil/počítač/jiný HC-05). Z pohledu psaní kódu tak nepotřebujeme žádnou speciální knihovnu, vystačíme si stejnými funkcemi standartní knihovny Serial, které jsme dosud používali ke komunikaci přes USB.

**Pozor:** Modul HC-05 Lze napájet 5V, ale jeho vnitřní logika je 3,3V, tedy na jeho Rx pin nesmíme přivést vyšší napětí. To je problém, protože Arduino, které používáme má 5V napájení a pokud bychom napřímo propojili Tx Arduina a Rx HC-05, mohli bychom bluetooth modul zničit. Jak na školním robotovi tak na gamepad shieldu je to vyřešeno tak, že je Tx pin Arduina připojen přes dělič napětí, který 5V Arduina sníží na 3,3V pro HC-05. Pokud však budete dělat vlastní zapojení, nezapomeňte toto ošetřit.

![image](https://github.com/user-attachments/assets/9278e36b-f683-4ed7-9d53-2fb4cdef2cd3)


Robot, bluetooth ovládání HC-05 UART bridge
Ukázka wifi?


## Gamepad shield
Pro pohodlné ovládání robota použijeme gamepad shield - přídavnou desku, která se nasadí na Arduino a obsahuje směrová tlačítka, joystick a řadu praktických konektorů, mimo jiné i na bluetooth modul.

![image](https://github.com/user-attachments/assets/69af4cfa-465f-42e0-b98b-f747f3309a82)

*Zdroj obrázku: https://wiki.keyestudio.com/Ks0153_keyestudio_JoyStick_Shield*

![image](https://github.com/user-attachments/assets/f425f131-3c2a-4fcb-ac9d-26fef8bae476)
*Připojení Bluetooth modulu*


