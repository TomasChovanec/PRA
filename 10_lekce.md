# 10 - Bluetooth

V dnešní lekci si ukážeme jak použít s Arduinem bezdrátovou komunikaci. Asi nejsnazší cestou je technologie Bluetooth. Je to 2,4GHz rádiový přenos určený na krátké vzdálenosti, který běžně používáme k připojení bezdrátových periferií jako sluchátek, reproduktorů, myší, klávesnic a mnoha dalšího. Dále můžeme s jeho pomocí například sbírat data ze senzorů nebo ovládat různá zařízení přes aplikaci na telefonu.

## HC-05
V této lekci budeme používat bluetooth modul HC-05, který je velmi rozšířený, pro svou nízkou cenu a jednoduchou obsluhu. Nevýhoda je, že podporuje pouze starší standard Bluetooth 2.0, a proto není kompatibilní s výrobky firmy Apple. Ovšem lze ho použít ke komunikaci s telefony Android, s notebooky či nevázat komunikaci mezi dvěma moduly HC-05.

## Použití
HC-05 funguje jako bezdrátový UART bridge. Tedy pokud ho připojíme k pinům Rx a Tx Arduina, všechna data, která prostřednictvím sériové linky pošleme, se přenesou bezdrátově do spárovaného zařízení (mobil/počítač/jiný HC-05). Z pohledu psaní kódu tak nepotřebujeme žádnou speciální knihovnu, vystačíme si stejnými funkcemi standartní knihovny Serial, které jsme dosud používali ke komunikaci přes USB.


Robot, bluetooth ovládání HC-05 UART bridge
Ukázka wifi?
