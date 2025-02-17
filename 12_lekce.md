## Arduino jako jednoduchý měřící přístroj
Arduino má mnoho vstupů, na kterých dokáže měřit jak digitálně stav logické 1 nebo 0, tak i několik analogových pinů, schopných měřit napětí od nuly do 5V. Lze ho tedy použít jako jednoduchý měřící přístroj. Může kontinuálně měřit data a posílat je do počítače, který už je dále zpracuje (uloží, zobrazí, vykreslí graf,...)

![image](https://github.com/user-attachments/assets/d388171d-3d0b-4923-83e2-bf263e34e9d4)

V této lekci si ukážeme, jak z arduina udělat jednoduchý osciloskop, vykreslíme průběh napětí na kondenzátoru při nabíjení a vybíjení.


## Serial Plotter     ![image](https://github.com/user-attachments/assets/745f94db-69d8-4204-b9f0-b735ca78a35f)

Pro zobrazování měřených dat máme možnost využít nástroj **Serial Plotter**, který je standartní součástí Arduino IDE (ikonka hned vedle Serial Monitoru). Na základní zobrazení signálu se dá použít, neumí ale třeba nastavit rozsah osy Y nebo zoomovat v zobrazeném grafu atd.

![image](https://github.com/user-attachments/assets/6a673e10-8fd6-433a-ba71-812124b480e4)

### Úkoly:
1. Připojte k Arduinu potenciometr, měřte na něm napětí funckí analogRead() a posílejte naměřená data po sériovíé lince. Pak je zobrazte pomocí Serial Plotteru v Arduino IDE
2. Přidejte druhý kanál - opačnou hodnotu potenciometru

## Better Serial Plotter
Pro více funkcí můžeme zkusit program [Better Serial Plotter](https://github.com/nathandunk/BetterSerialPlotter) ke stažení [zde](https://github.com/nathandunk/BetterSerialPlotter/releases/download/v0.1.2/BetterSerialPlotter-v0.1.2-Windows.zip)

V programu stačí vybrat sériový port, na kterém je připojeno Ardino. Formát dat je stejný jako pro Serial Plotter - stačí tedy posílat pokaždé jeden řádek dat, pokud je čísel více, mohou být odděleny mezerou.

:warning: Protože v jednu chvíli může být k sériovému portu připojen jen jeden program, ve chvíli, kdy zobrazujete data v Serial plotteru, nemůžete do Arduina nahrát nový program. Je nutné vždy předtím Serial plotter buď zavřít, nebo v něm nastavit jiný port.

![image](https://github.com/user-attachments/assets/41677a14-07b7-466c-8c68-02acaf63060b)


### Úkol:
1. Použijte program Better Serial Plotter pro zobrazení dat z potenciometru


## Kondenzátor

:warning: U elektrolytického kondenzátoru musíme dodržet správnou polaritu, jinak dojde ke zničení kondenzátoru s možnou [explozí](https://www.youtube.com/watch?v=rr7bPmGTQUk&ab_channel=ElectroBOOM)


### Úkoly:
**1.** Zapojit LEDku a odpor + jeden sériový odpor navíc

**2.** Zkusit blikat připojením k 5V

![image](https://github.com/user-attachments/assets/20e18b1d-2c97-4652-bbfd-3743ce62271a)

**3.** Připojit k LEDce a jednomu odporu paralelně kondenzátor

**4.** Zkoušejte připojovat odpojovat napájecí napětí, Pohrajte si, pochopte co se děje

**5.** Blikat 13pinem s LEDkou s kondíkem

**6.** Měřit 13pin a napětí na kondíku

**7.** AnalogWrite - > přes rezistor na kondík, řídit potenciometrem

## Další užitečné články a videa

[Video o kondenzátorech](https://www.youtube.com/watch?v=K_MFUkW1-Qo&ab_channel=N%C3%A1zorn%C3%A1elektrotechnika) (a o tom, proč některé vybuchují při nesprávné polaritě)
