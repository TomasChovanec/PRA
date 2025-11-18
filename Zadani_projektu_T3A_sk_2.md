## Termín 8.1., odevzdání dokumentace emailem nejpozději 6.1. 23:59

### Radim P., Ivan R. - Otevírání dveří na RFID karty
- Pomocí Arduina a RFID modulu připravte projekt pro otevírání dveří kartou. 
- Po přiložení karty, která je v seznamu přístupů se dveře otevřou (otevření zámku simulujte pohybem serva)
- Na OLED displeji se bude zobrazovat informace o tom, zda je karta načtena a zda je povolená
- Seznam povolených karet by měl být implementovaný tak, aby se do něj snadno daly přidávat další karty.

### Tomáš S., Vilém S. - Reklamní banner s maticovým displejem
- Pomocí Arduina a maticového displeje vytvořte reklamní banner
- Text zobrazovaný na banneru se bude nastavovat přes Serial monitor
- Dále bude možné přes serial monitor nastavit rychlost a směr rotace textu
- Bude možné kromě textu zobrazit i jednoduchý obrázek

### Jan S. - Hra s OLED displejem a akcelerometrem
- ???

### Denis. M. - Elektronická hrací kostka
- Pomocí Arduina, OLED displeje a tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na displeji budou měnit obrázky kostky s různými hodnotami
- Po puštění tlačítka se hodnota zastaví

### Marek. O.-  Elektronická hrací kostka
- Pomocí Arduina, LCD displeje a RGB LEDky vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na displeji budou velmi rychle měnit náhodné hodnoty 1-6.
- Po puštění tlačítka se hodnota zastaví
- Každé hodnotě bude odpovídat jedna barva. Podle toho, jaké číslo "padne" na kostce se zbarví RGB LEDka


## Termín 22.1., odevzdání dokumentace emailem nejpozději 20.1. 23:59§

### Tomáš T. -  Elektronická hrací kostka
- Pomocí Arduina, LED diod a tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty.
- Po puštění tlačítka se hodnota zastaví

### Tomáš M.- Hodinky s budíkem a stopkami
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktuálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení
- Když se čas shoduje s časem budíku, ozve se melodie z piezo buzzeru

### Petr M., Jiří S. - Robot jako sledovač čáry s funkcí objetí překážky
Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)

### Libor R., Lukáš M. - Elektronické piano 
Pomocí Arduina pieza a 5 tlačítek vytvořte jednoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie
- Na OLED displeji se bude zobrazovat aktuálně přehrávaný tón

### Tadeáš V., Stanislav P. - Hra na postřeh pro dva hráče
Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se zhasne LEDka a pak se po náhodném časovém intervalu rozsvítí
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší
