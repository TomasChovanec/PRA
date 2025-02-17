## Arduino jako jednoduchý měřící přístroj
![image](https://github.com/user-attachments/assets/d388171d-3d0b-4923-83e2-bf263e34e9d4)
- Arduino má několik digitálních a analogvých vstupů, dá se tedy použít jako jednoduchý měřící přístroj. Může kontinuálně měřit data a posílat je do počítače, který už je dále zpracuje (uloží, zobrazí, vykreslí graf,...)
- Ukážeme si jak z arduina udělat jednoduchý osciloskop, vykreslíme průběh napětí na kondenzátoru při nabíjení a vybíjení


## Serial Plotter     ![image](https://github.com/user-attachments/assets/745f94db-69d8-4204-b9f0-b735ca78a35f)

- Můžeme Arduino použít k měření hodnot, ty posílat do PC a tam dále zpracovávat
- Pro zobrazování kontinuálních hodnot můžeme použít **Serial Plotter** v Arduino IDE (ikonka hned vedle Serial Monitoru). Ten ale má jen velmi omezené funkce.

![image](https://github.com/user-attachments/assets/6a673e10-8fd6-433a-ba71-812124b480e4)

## Better Serial Plotter
Zkusíme použít [Better Serial Plotter](https://github.com/nathandunk/BetterSerialPlotter) ke stažení [zde](https://github.com/nathandunk/BetterSerialPlotter/releases/download/v0.1.2/BetterSerialPlotter-v0.1.2-Windows.zip)

Ten nám nabídne více funkcí, jako úpravu rozsahu os x a y, přehlednější zobrazení, rozdělení do více grafů atd.

![image](https://github.com/user-attachments/assets/41677a14-07b7-466c-8c68-02acaf63060b)


### Úkoly:
1. Posílejte naměřená data z potenciometru
2. Přidejte druhý kanál - opačnou hodnotu potenciometru


## Kondenzátor
- :warning: U elektrolytického kondenzátoru musíme dodržet správnou polaritu, jinak dojde ke zničení kondenzátoru s možnou [explozí](https://www.youtube.com/watch?v=rr7bPmGTQUk&ab_channel=ElectroBOOM)
- :star: Zapojit LEDku a odpor + jeden sériový odpor navíc
- :star: :star: Zkusit blikat připojením k 5V
- :star: :star: :star:Připojit k LEDce a jednomu odporu paralelně kondenzátor
- :crown: Zkoušejte připojovat odpojovat napájecí napětí, Pohrajte si, pochopte co se děje

### Úkoly:
1. Blikat 13pinem s LEDkou s kondíkem
2. Měřit 13pin a napětí na kondíku
3. AnalogWrite - > přes rezistor na kondík, řídit potenciometrem![image](https://github.com/user-attachments/assets/4ac69565-68c5-493c-869d-f8647295048c)

## Další užitečné články a videa

[Video o kondenzátorech](https://www.youtube.com/watch?v=K_MFUkW1-Qo&ab_channel=N%C3%A1zorn%C3%A1elektrotechnika) (a o tom, proč některé vybuchují při nesprávné polaritě)
