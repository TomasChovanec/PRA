### Mi.Pr. - Ruleta
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md) do **29.1. 23:59**
- :heavy_check_mark: Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **10.2. 23:59**
- :heavy_check_mark: Prezentace ve škole  **12.2.**

**Zadání:**
- Na OLED displeji zobrazte ilustrační obrázek rulety.
- Krátkým stiskem tlačítka spusťte roztočení rulety; na displeji se rychle střídají čísla a postupně se zpomalují.
- Po zastavení se na displeji zobrazí výsledné číslo a text „VÝSLEDEK“.
- RGB LED signalizuje výsledek: zelená = 0, červená = červené číslo, modrá = černé číslo.

--- 

### Ad.Se. - Hra na postřeh pro dva hráče
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md) do **29.1. 23:59**
- :heavy_check_mark: Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **10.2. 23:59**
- :heavy_check_mark: Prezentace ve škole  **12.2.**

**Zadání:**
- Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se zhasne LEDka a pak se po náhodném časovém intervalu rozsvítí
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

--- 

### Ja.Po. - Ovládání výtahu Arduinem
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md) do **29.1. 23:59**
- :heavy_check_mark: Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **10.2. 23:59**
- :heavy_check_mark: Prezentace ve škole  **12.2.**

**Zadání:**
- Vytvořte s Arduinem simulaci výtahu. Bude obsahovat krokový motor, OLED displej a klávesnici pro volbu patra.
- Po stisku tlačítka se na displeji zobrazí na 2s instrukce k ukončení nástupu a odstoupení z prostoru dveří
- Poté se krokový motor začne otáčet, směr otáčení závisí na tom, zda jede nahoru nebo dolů. Jednomu patru bude odpovídat jedna celá otáčka hřídele.
- Během jízdy bude na displeji bude zobrazovat aktuální polohu výtahu a šipku směru jízdy (nahoru/dolů)
- Pokud bude během jízdy výtahu stisknuto další tlačítko, výtah nejprve dojede do původního cíle a po času na vystoupení se rozjede do nového cíle

--- 

### Da.Šp. - Elektronická kostka s LEDkami
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md) do **29.1. 23:59**
- :heavy_check_mark: Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **10.2. 23:59**
- :heavy_check_mark: Prezentace ve škole  **12.2.**

**Zadání:**
- Pomocí Arduina, 7ks LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty. 
- Po puštění tlačítka se hodnota zastaví

--- 

### To.Ře - Elektronické piano
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md)  do **29.1. 23:59**
- Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **17.2. 23:59**
- Prezentace ve škole  **19.2.**

**Zadání:**
- Pomocí Arduina pieza a alespoň 6 tlačítek vytvořte jednoduché “piano”.
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie

--- 

### Mi.Sa. - Elektronický dveřní zámek s otevíráním na kód a na čip
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md)  do **29.1. 23:59**
- Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **17.2. 23:59**
- Prezentace ve škole  **19.2.**

 **Zadání:**
- Vytvořte elektronický dveřní zámek ovládaný číselným kódem z klávesnice nebo RFID čipem.
- Zadaný kód / přiložený čip porovnejte s uloženými hodnotami a rozhodněte o povolení či zamítnutí vstupu.
- Na LCD displeji zobrazujte stav systému (zadejte kód, přístup povolen / zamítnut).
- Zelená LED signalizuje odemčení, červená LED zamknutí; bzučák akusticky potvrdí výsledek.
- Po třech chybných pokusech zámek zablokujte na 20 sekund.

--- 

### Ji.Pš. Dino game
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md)  do **29.1. 23:59**
- Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **17.2. 23:59**
- Prezentace ve škole  **19.2.**

**Zadání:**
- Pomocí Arduina a LCD 2×16 vytořte jednoduchou hru typu Dino game: dinosaurus běží zleva doprava a proti němu se objevují překážky.
- Pomocí tlačítka umožněte skok dinosaura. Při skoku se dinosaurus zobrazí v horním řádku LCD.
- Překážky se pohybují z pravé strany displeje doleva a jejich rychlost se postupně zvyšuje.
- Při srážce dinosaura s překážkou hra končí a na displeji se zobrazí „GAME OVER“ a skóre.
- Hra nepoužívá pro časování hlavní herní smyčky delay() a je řízena pomocí času (millis()).

--- 

### Ja.Su. - Otevírání dveří na RFID karty
**Termíny:**
- :heavy_check_mark: [Kontrola HW](Kontrola_HW.md)  do **29.1. 23:59**
- Odevzdání [dokumentace](Projekt.md#hodnocení) mailem do **17.2. 23:59**
- Prezentace ve škole  **19.2.**

**Zadání:**
- Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Na OLED displeji se bude zobrazovat informace o tom, zda je karta načtena a zda je povolená
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

