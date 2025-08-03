## Zadání projektů

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 

### Nápojový automat na RFID karty
Automat bude obsahovat displej, 4 tlačítka, RFID modul a bzučák.
- Po přiložení karty nebo čipu se na chvíli zobrazí na displeji jméno majitele a zbývající kredit (popř. upozornění na neznámého uživatele)
- Poté se zobrazí nabídka nápojů s cenou
- Uživatel vybere pomocí tlačítek nápoj, pokud má dostatečný kredit nápoj se připraví a vydá
- Příprava nápoje bude simulována zvuky z bzučáku, po dokončení přípravy se ozve krátký vysoký tón
- Cena nápoje se strhne uživateli z kreditu
- Informace o výši kreditu jednotlivých uživatelů musí být zachována i po vypnutí napájení (použijte EEPROM)

### Alarm 
Alarm bude obsahovat pohybové čidlo, bzučák a klávesnici.
- Po stisknutí hvězdičky se spustí alarm
- Deset sekund po spuštění alarmu bude blikat rychle LEDka, jako indikace toho, že obsluha má odejít z hlídaného prostoru
- Po těchto 10s začne LEDka blikat pomalu a aktivuje se pohybové čidlo
- Pokud pohybové čidlo zachytí pohyb, opět se rozbliká LEDka a pokud se do 10s na klávesnici nezadá správný 4místný kód, začne houkat alarm

### Elektronické piano
Pomocí Arduina pieza a alespoň 5 tlačítek vytvořte jedoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie

### Automatické otvírání brány
Vytvořte program a zrealizuj zapojení pro Arduino, které automaticky otevře bránu, když k ní přijede auto a po projetí ji opět zavře. Požadované funkce:
- Dokud není detekováno auto, brána je zavřená.
- Po detekci auta se brána otevře.
- Dokud auto stojí před branou, brána zůstává otevřená. Teprve až auto projede, brána se zavře.
- Pokud by ale auto neprojelo do 30s, brána se zavře.
- Jako bezpečnostní prvek, aby nedošlo ke zranění případných chodců, před započetím pohybu (otvírání nebo zavírání) 5x blikne červené výstražné světlo a 5x zazní varovný zvukový signál.

### Teploměr a vlhkoměr
Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. 
Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.

### RFID čtečka pro otvírání dveří
Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Ovládání LEGO robota Arduinem
Upravte LEGO robota tak, aby jej šlo řídit Arduinem.
- Připoravte ovládání motoru pohonu a serva pro zatáčení
- Připojte k Arduinu bezdrátový modul a naprogramujte Arduino tak, aby vykonávalo povely z dálkového ovládání

### Elektronická kostka

### Elektronická kostka
Pomocí Arduina, displeje a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku se na displeji velmi rychle budou měnit hodnoty. 
 - Při puštění se hodnota zobrazí
 - Pokud padne šestka, hází program sám ještě jednou a zobrazí např 6+6=12


### Robot Line follower

Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)

### Parkovací čidlo

Pomocí Arduina, pieza a ulrtazvukového senzoru vytvořte parkovací senzor pro auto
- Senzor je aktivní pouze když je stisknuto tlačítko (simulujeme spínač na zpátečce v autě)
- Když je překážka vzdálena více než 100 cm, bzučák nebude vydávat žádný zvuk.
- Pokud se překážka nachází mezi 100 cm a 50 cm, bzučák vydá krátký zvuk jednou za sekundu.
- Když se překážka přiblíží na 50–20 cm, pípání bude jednou za půl sekundy.
- Pokud je překážka blíže než 20 cm, bzučák bude pípat neustále.

### Piano
Pomocí Arduina pieza a alespoň 4 tlačítek vytvořte jedoduché "piano". 
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Po stisku dvou tlačítek současně se přehraje přednastavená melodie.


### Elektronický zámek
Pomocí Arduina vytvořte elektronický zámek s klávesnicí, displejem a servem
- Zámek se bude otevírat čtyřmístným číselným kódem potvrzeným křížkem
- Po 3 chybných zadáních se zámek na 10s zablokuje (odpočet bude na displeji)
- Projekt bude umožňovat změnu kódu bez změny programu (bez nutnosti nahrát znovu kód do arduina)

### Automatické otevírání kurníku
Pomocí Arduina, fotorezistoru a krokového motoru vytvořte automatické ovládání vrátek do kurníku v závislosti na slunečním svitu.
- Ošetřete například případy, kdy čidlo někdo krátkodobě zakryje rukou, nebo na něj naopak krátkodobě zasvítí např. světlo projíždějícího auta




### Otevírání dveří na RFID karty (Jakub. J.)
- Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Na OLED displeji se bude zobrazovat informace o tom, zdsa je karta načtena a zda je povolená
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Elektronické piano (Jan. J.)
- Pomocí Arduina, pieza a alespoň 8 tlačítek vytvořte jedoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Budou k dispozici dvě další tlačítka, jejichž stiskem se spustí jedna ze tří přednastavených melodií.

### Elektronická kostka (F.D.)
- Pomocí Arduina, LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty. 
- Po puštění tlačítka se hodnota zastaví 

### Hra na postřeh 2 hráče (J.H.)
- Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se postupně rozsítí všechny LED a pak po náhodném intervalu zhasnou
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Hodiny, stopky (E.K.)
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení

### MP3 přehrávač s BT ovládáním (A.K.)
- Sestrojte a naprogramujte jednoduchý MP3 přehrávač, který přehrává hudbu z SD karty 
- Ovládání přes tlačítka, možnost play/pause, přepnutí na další skladbu
- Zobrazování stavu přehrávače na OLED displeji

### "Bomba" s časovačem (M.J.)
 - Navrhněte a naprogramujte zařízení, které simuluje bombu s časovačem.
 - Bomba má být aktivována tlačítkem, zobrazovat odpočet, a může být deaktivována zadáním správného kódu na klávesnici.
 - Při aktivaci a deaktivaci hraje zvukové efekty pomocí MP3 modulu.


### Alarm s IR ovládáním (T.D.)
 - Navrhněte a naprogramujte alarm ovládaný přes infračervené rozhranní
 - Po zakódování pomocí IR vysílače Arduino sleduje stav dveřního spínače
 - Pokud se dvěřní spínač otevře a do 5 sekund nedojde k deaktivaci IR kódem, rozezní se alarm pomocí piezza

