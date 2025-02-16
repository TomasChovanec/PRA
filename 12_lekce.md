## Arduino jako měřící přístroj
- Arduino má několik digitálních a analogvých vstupů, dá se tedy použít jako jednoduchý měřící přístroj. Může kontinuálně měřit data a posílat je do počítače, který už je dále zpracuje (uloží, zobrazí, vykreslí graf,...)
- Ukážeme si jak z arduina udělat jednoduchý osciloskop, vykreslíme průběh napětí na kondenzátoru při nabíjení a vybíjení

## Serial plotter
- Můžeme Arduino použít k měření hodnot, ty posílat do PC a tam dále zpracovávat
- Pro zobrazování kontinuálních hodnot můžeme použít serial plotter v Arduino IDE, ale má jen velmi omezené funkce
- Zkusíme použít [Better Serial Plotter](https://github.com/nathandunk/BetterSerialPlotter) ke stažení [zde](https://github.com/nathandunk/BetterSerialPlotter/releases/download/v0.1.2/BetterSerialPlotter-v0.1.2-Windows.zip)

### Úkoly:
1. Posílejte naměřená data z potenciometru
2. Přidejte druhý kanál - opačnou hodnotu potenciometru



## Kondenzátor

- :warning: U elektrolytického kondenzátoru musíme dodržet správnou polaritu, jinak dojde ke zničení kondenzátoru s možnou [explozí](https://www.youtube.com/watch?v=rr7bPmGTQUk&ab_channel=ElectroBOOM)
- Zapojit LEDku a odpor + jeden sériový odpor navíc
- Zkusit blikat připojením k 5V
- Připojit k LEDce a jednomu odporu paralelně kondenzátor
- Zkoušejte připojovat odpojovat napájecí napětí, Pohrajte si, pochopte co se děje

