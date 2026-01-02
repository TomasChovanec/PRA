## Termín prezentace ve škole: 18.12., termín odevzdání dokumentace mailem: 16.12. 23:59

### :x: Adam H. - Prodejní automat na RFID karty
Automat bude obsahovat displej, 4 tlačítka, RFID modul a bzučák.
- Po přiložení karty nebo čipu se na chvíli zobrazí na displeji jméno majitele a zbývající 
kredit (popř. upozornění na neznámého uživatele)
- Poté se zobrazí nabídka nápojů s cenou
- Uživatel vybere pomocí tlačítek nápoj, pokud má dostatečný kredit nápoj se připraví a 
vydá
- Příprava nápoje bude simulována zvuky z bzučáku, po dokončení přípravy se ozve krátký 
vysoký tón
- Cena nápoje se strhne uživateli z kreditu. Informace o kreditu může být uložena v Arduinu nebo na kartě (vyber dle uvážení, výhody a nevýhody uveď v závěru).


### :white_check_mark: Josef K.  - Elektronický zámek
Pomocí Arduina vytvořte elektronický zámek s klávesnicí, displejem a servem
- Zámek se bude otevírat čtyřmístným číselným kódem potvrzeným křížkem
- Po 3 chybných zadáních se zámek na 10s zablokuje (odpočet bude na displeji)
- Projekt bude umožňovat změnu kódu bez změny programu (bez nutnosti nahrát znovu kód do arduina)

### :white_check_mark: Dominik G. - Parkovací senzor
Pomocí Arduina, pieza a ultrazvukového senzoru vytvořte parkovací senzor pro auto
- Senzor je aktivní pouze když je stisknuto tlačítko (simulujeme spínač na zpátečce v autě)
- Když je překážka vzdálena více než 100 cm, bzučák nebude vydávat žádný zvuk.
- Pokud se překážka nachází mezi 100 cm a 50 cm, bzučák vydá krátký zvuk jednou za sekundu.
- Když se překážka přiblíží na 50–20 cm, pípání bude jednou za půl sekundy.
- Pokud je překážka blíže než 20 cm, bzučák bude znít neustále.
  
### :white_check_mark: Richard F.
Pomocí ultrazvukového senzoru HC-SR04, Arduina a tlačítek vytvořte zařízení, které změří délku a šířku objektu a vypočítá plochu.
- Měřená hodnota se průběžně zobrazuje na displeji, stiskem tlačítka se potvrdí a přejde se na měření další hodnoty
- Po zadání všech hodnot se zobrazí všechny naměřené hodnoty spolu s výslednou plochou

### :white_check_mark: Dan L. - Teploměr a vlhkoměr
Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. 
Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.
  
### :white_check_mark: Jakub Kr. - Elektronické piano
Pomocí Arduina pieza a alespoň 5 tlačítek vytvořte jednoduché “piano”.

Po stisku tlačítka se přehraje příslušný tón.
Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
Při stisku dvou tlačítek najednou se spustí předem nastavená melodie


## Termín prezentace ve škole: 15.1., termín odevzdání dokumentace mailem: 13.1. 23:59

### Marek H. - Univerzální senzory s mikrokontrolérem XIAO ESP32c6 pro chytrou domácnost s komunikací přes Zigbee protokol
- Kompletace univerzálních desek plošného spoje s ESP32c6
    - BME680 pro teplotu, tlak, vlhkost, stav vzduchu
    - PIR senzor pro detekci pohybu
    - Fotorezistor pro detekci osvětlení místnosti
    - Siréna pro upozorňení na krizové situace
    - Ostatní piny vyvedeny na dutinky pro připojení externích senzorů (wattmetry, detekce zavření oken, dveří, detekce hladiny vody, teplota v kotli, bojleru apod.)
    - Bateriové napájení pro případ vypadnutí proudu
- 3D modelování krabičky a uchycení zařízení
- Komunikace přístrojů s HomeAssistantem na Raspberry Pi přes Zigbee protokol (ESPIDF)  - mashová struktura, jednotlivé zařízení nemusí být připojena na hlavní router, pouze na další Zigbee zařízení (jiný node)
- Pro prezentaci ve škole - ukázka komunikace a výměny dat v Zigbee protokolu mezi dvěma zařízeními, ukázka kódu v ESPIDF

### Petr K. - Hodiny, stopky, budík
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktuálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení
- Když se čas shoduje s časem budíku, ozve se melodie z piezo buzzeru

### Jakub Ku. - Had
- Pomocí Arduina, OLED displeje a joysticku vytvořte hru Had

### Dominik K., Daniel F. - Hra na postřeh 2 hráče 
- Pomocí Arduina a OLED displeje vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se zhasne LEDka a pak se po náhodném časovém intervalu rozsvítí
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole se na OLED displayi ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Matouš K. - Robotická ruka
- Vytvořte program a zapojení pro posílení pohybu ruky servem
- K projektu přidejte OLED displej se zobrazením času a hrou

### Max F., Matouš G. - Elektronická hrací kostka
- Pomocí Arduina, sedmisegmentového displeje a tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na displeji budou velmi rychle měnit náhodné hodnoty.
- Při každé změně čísla se zároveň i náhodně změní pozice čísla na displeji
- Po puštění tlačítka se hodnota zastaví
  
### Vít K. - Hudební přehrávač s dálkovým ovládáním
- Pomocí dvou Arduin a mp3 modulu vytvořte hudební přehrávač
- Dálkový ovladač bude představovat druhé Arduino. Bude umožňovat funkce spuštění přehrávání, pauzu a přechod na další skladbu.
- Spojení mezi ovladačem a přehrávačem může být buď drátové nebo bezdrátové (Bluetooth)

