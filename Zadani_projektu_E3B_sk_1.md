## Zadání projektů E3B skupina 1

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 

### Robot line follower

Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)

### Automatické otvírání brány

Vytvořte program a zrealizujte zapojení pro Arduino, které automaticky otevře bránu, když k ní přijede auto a po projetí ji opět zavře. Požadované funkce:
- Dokud není detekováno auto, brána je zavřená.
- Po detekci auta se brána otevře.
- Dokud auto stojí před branou, brána zůstává otevřená. Teprve až auto projede, brána se zavře.
- Pokud by ale auto neprojelo do 30s, brána se zavře.
- Jako bezpečnostní prvek, aby nedošlo ke zranění případných chodců, před započetím pohybu (otvírání nebo zavírání) 5x blikne červené výstražné světlo a 5x zazní varovný zvukový signál.

### Vánoční osvětlení

Pomocí Arduina, LED diod vytvořte dekorativní osvětlení s několika módy blikání, které lze měnit tlačítkem
- Liché LEDky jsou zhasnuté, sudé se plynule rozsvěcejí, až se rozsvítí doplna, plynule se rozsvítí liché LEDky  a opačně plynule zhasnou nejprve liché, pak sudé
- Všechny LEDky jsou zhasnuté, jedna rozsvícená LEDka "jezdí" zleva doprava
- Další alespoň dva módy dle vlastního výběru
- Pro tvorbu kódu používejte for cyklus

### Teploměr a vlhkoměr

Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. 
Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.

### Elektronická hrací kostka

Pomocí Arduina, displeje, LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku tlačítka se na displeji velmi rychle budou měnit náhodné hodnoty. 
- Při puštění tlačítka se hodnota zobrazí
- Hodnota se kromě displeje zobrazí i na LEDkách ve stejném tvaru jako na kostce

### RFID čtečka pro otvírání dveří

Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Vánoční osvětlení

Pomocí Arduina, 10LED diod a potenciometru vytvořte dekorativní osvětlení s několika módy blikání, které lze měnit tlačítkem
- Liché LEDky jsou zhasnuté, sudé se plynule rozsvěcejí, až se rozsvítí doplna, plynule se rozsvítí liché LEDky  a opačně plynule zhasnou nejprve liché, pak sudé
- Všechny LEDky jsou zhasnuté, postupně se rozsvěcují zleva doprava a pak zase zhasínají zprava doleva. Potenciometrem lze nastavit rychlost efektu
- Další alespoň dva módy dle vlastního výběru
- Pro tvorbu kódu používejte for cyklus

### Parkovací senzor

Pomocí Arduina, pieza a ultarzvukového senzoru vytvořte parkovací senzor pro auto
- Senzor je aktivní pouze když je stisknuto tlačítko (simulujeme spínač na zpátečce v autě)
- Když je překážka vzdálena více než 100 cm, bzučák nebude vydávat žádný zvuk.
- Pokud se překážka nachází mezi 100 cm a 50 cm, bzučák vydá krátký zvuk jednou za sekundu.
- Když se překážka přiblíží na 50–20 cm, pípání bude jednou za půl sekundy.
- Pokud je překážka blíže než 20 cm, bzučák bude pípat neustále.


