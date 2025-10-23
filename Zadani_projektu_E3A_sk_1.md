### Hra Tetris (Vojtěch 30.10.)
- Pomocí Arduina, čtyř 8x8 maticových displejů a joysticku vytvořte hru Tetris


### Hra na postřeh 2 hráče (Jonáš 6.11.)
- Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se zhasne LEDka a pak se po náhodném časovém intervalu rozsvítí
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší


### Otevírání dveří na RFID karty (Martin 6.11.)
- Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Na OLED displeji se bude zobrazovat informace o tom, zda je karta načtena a zda je povolená
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.


### Elektronický zámek (Rostislav 6.11.)
Pomocí Arduina vytvořte elektronický zámek s klávesnicí, displejem a servem
- Zámek se bude otevírat čtyřmístným číselným kódem potvrzeným křížkem
- Po 3 chybných zadáních se zámek na 10s zablokuje (odpočet bude na displeji)
- Projekt bude umožňovat změnu kódu bez změny programu (bez nutnosti nahrát znovu kód do arduina)


### Elektronické piano (Adam 13.11.)
Pomocí Arduina pieza a alespoň 5 tlačítek vytvořte jedoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie


### Ultrazvukový senzor vzdálenosti s výpočtem plochy (Dominik 13.11.)
- Pomocí ultrazvukového senzoru HC-SR04, Arduina a tlačítek vytvořte zařízení, které změří délku a šířku objektu a vypočítá plochu.
- Měřená hodnota se průběžne zobrazuje na displeji, stiskem tlačítka se potvrdí a přejde se na měření další hodnoty
- Po zadání všech hodnot se zobrazí všechny naměřené hodnoty spolu s výslednou plochou


### Elektronická kostka (Ondřej 13.11.)
- Pomocí Arduina, sedmisegmentového displeje a tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na displeji budou velmi rychle měnit náhodné hodnoty. 
- Po puštění tlačítka se hodnota zastaví


### Herní konzole(Filip 13.11.)
- Pomocí Arduina, OLED displeje a joysticku vytvořte herní konzoli s hrami: Snake, Tetris popř. další
