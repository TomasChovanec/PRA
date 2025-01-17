## Zadání projektů E3A skupina 2

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 


### Matěj S. - Nápojový automat na RFID karty
Automat bude obsahovat displej, 4 tlačítka, RFID modul a bzučák.
- Po přiložení karty nebo čipu se na chvíli zobrazí na displeji jméno majitele a zbývající kredit (popř. upozornění na neznámého uživatele)
- Poté se zobrazí nabídka nápojů s cenou
- Uživatel vybere pomocí tlačítek nápoj, pokud má dostatečný kredit nápoj se připraví a vydá
- Příprava nápoje bude simulována zvuky z bzučáku, po dokončení přípravy se ozve krátký vysoký tón
- Cena nápoje se strhne uživateli z kreditu
- Informace o výši kreditu jednotlivých uživatelů musí být zachována i po vypnutí napájení (použijte EEPROM)

### Matyáš M. - Alarm 
Alarm bude obsahovat pohybové čidlo, bzučák a klávesnici.
- Po stisknutí hvězdičky se spustí alarm
- Deset sekund po spuštění alarmu bude blikat rychle LEDka, jako indikace toho, že obsluha má odejít z hlídaného prostoru
- Po těchto 10s začne LEDka blikat pomalu a aktivuje se pohybové čidlo
- Pokud pohybové čidlo zachytí pohyb, opět se rozbliká LEDka a pokud se do 10s na klávesnici nezadá správný 4místný kód, začne houkat alarm

### Jiří K. - Elektronické piano
Pomocí Arduina pieza a alespoň 5 tlačítek vytvořte jedoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie

### Luděk L. - Automatické otvírání brány
Vytvořte program a zrealizuj zapojení pro Arduino, které automaticky otevře bránu, když k ní přijede auto a po projetí ji opět zavře. Požadované funkce:
- Dokud není detekováno auto, brána je zavřená.
- Po detekci auta se brána otevře.
- Dokud auto stojí před branou, brána zůstává otevřená. Teprve až auto projede, brána se zavře.
- Pokud by ale auto neprojelo do 30s, brána se zavře.
- Jako bezpečnostní prvek, aby nedošlo ke zranění případných chodců, před započetím pohybu (otvírání nebo zavírání) 5x blikne červené výstražné světlo a 5x zazní varovný zvukový signál.

### Jakub K. - Teploměr a vlhkoměr
Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. 
Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.

### Matyáš L. - RFID čtečka pro otvírání dveří
Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Šimon P. - Ovládání LEGO robota Arduinem
Upravte LEGO robota tak, aby jej šlo řídit Arduinem.
- Připoravte ovládání motoru pohonu a serva pro zatáčení
- Připojte k Arduinu bezdrátový modul a naprogramujte Arduino tak, aby vykonávalo povely z dálkového ovládání

### Tomáš R. - Elektronická kostka
Pomocí Arduina, LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty. 
- Při puštění tlačítka se hodnota zastaví
