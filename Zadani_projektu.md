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

### Teploměr a vlhkoměr
Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. 
Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.

### Robot Line follower
Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)

### Elektronický zámek
Pomocí Arduina vytvořte elektronický zámek s klávesnicí, displejem a servem
- Zámek se bude otevírat čtyřmístným číselným kódem potvrzeným křížkem
- Po 3 chybných zadáních se zámek na 10s zablokuje (odpočet bude na displeji)
- Projekt bude umožňovat změnu kódu bez změny programu (bez nutnosti nahrát znovu kód do arduina)

### Otevírání dveří na RFID karty 
- Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Na OLED displeji se bude zobrazovat informace o tom, zdsa je karta načtena a zda je povolená
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Elektronická kostka
- Pomocí Arduina, LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty. 
- Po puštění tlačítka se hodnota zastaví 

### Hra na postřeh 2 hráče
- Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se postupně rozsítí všechny LED a pak po náhodném intervalu zhasnou
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Hodiny, stopky
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení

### MP3 přehrávač s BT ovládáním
- Sestrojte a naprogramujte jednoduchý MP3 přehrávač, který přehrává hudbu z SD karty 
- Ovládání přes tlačítka, možnost play/pause, přepnutí na další skladbu
- Zobrazování stavu přehrávače na OLED displeji

### "Bomba" s časovačem (M.J.)
 - Navrhněte a naprogramujte zařízení, které simuluje bombu s časovačem.
 - Bomba má být aktivována tlačítkem, zobrazovat odpočet, a může být deaktivována zadáním správného kódu na klávesnici.
 - Při aktivaci a deaktivaci hraje zvukové efekty pomocí MP3 modulu.

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

### Ovládání robota přes Bluetooth
Vytvořte program pro školního robota, aby jej bylo možné ovládat přes Bluetooth. Použijte Bluetooth modul HC-05 a robota ovládejte aplikací z telefonu.
- Program bude umožňovat manuální ovládání, kdy se pohyb robota řídí výhradně ovládáním z telefonu
- Dále zde bude autonomní režim, kdy robot bude jezdit rovně a pomocí ultrazvukového čidla detekovat překážky. Když detekuje překážku, otočí se a pojede jinam
- Autonomní a manuální režim bude možné přepínat z telefonu
- Po resetu bude robot v manuálním módu, do autonomního se přepne buď povelem z telefonu nebo stiskem tlačítka na robotovi.

### Ovládání výtahu
Vytvořte s Arduinem simulaci výtahu. Bude obsahovat krokový motor, servo, displej a tlačítka pro volbu patra.
- Po stisku tlačítka se výtah rozjede, na displeji bude zobrazovat aktuální polohu
- Servo bude simulovat ovládání dveří

### Hra na postřeh
Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se v náhodném intervalu rozsvítí LEDka
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na displeji zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Řízení akvária
Připravte program pro Arduino, který bude spínat osvětlení akvária podle nastaveného času. Dále bude měřit a na displeji zobrazovat teplotu v akváriu.

### Voltmetr
- Pomocí Arduina vytvořte multimetr
- Alespoň dva napěťové rozsahy
- Měření proudu pomocí obvodu INA219

### Ultrazvukový senzor vzdálenosti s výpočtem plochy
- Pomocí ultrazvukového senzoru HC-SR04, Arduina a tlačítek vytvořte zařízení, které změří délku a šířku objektu a vypočítá plochu.
- Měřená hodnota se průběžne zobrazuje na displeji, stiskem tlačítka se potvrdí a přejde se na měření další hodnoty
- Po zadání všech hodnot se zobrazí všechny naměřené hodnoty spolu s výslednou plochou

### Regulace ventilátoru
- Pomocí teplotního čidla a Arduina ovládejte otáčky ventilátoru v závislosti na aktuální teplotě.
- Pod 25 °C: ventilátor vypnutý
- 25–30 °C: 30–60 % výkonu
- Nad 30 °C: 100 % výkonu
- Aktuální hodnotu teploty a PWM posílejte na Serial monitor
