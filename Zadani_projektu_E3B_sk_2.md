## Zadání projektů E3B skupina 2

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 

### Nápojový automat na RFID karty
Automat bude obsahovat displej, 4 tlačítka, RFID modul a bzučák.
- Po přiložení karty nebo čipu se na chvíli zobrazí na displeji jméno majitele a zbývající kredit (popř. upozornění na neznámého uživatele)
- Poté se zobrazí nabídka nápojů s cenou
- Uživatel vybere pomocí tlačítek nápoj, pokud má dostatečný kredit nápoj se připraví a vydá
- Příprava nápoje bude simulována zvuky z bzučáku, po dokončení přípravy se ozve krátký vysoký tón
- Cena nápoje se strhne uživateli z kreditu
- Informace o výši kreditu jednotlivých uživatelů musí být zachována i po vypnutí napájení (použijte EEPROM)

### Elektronická hrací kostka
Pomocí Arduina, displeje a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku se na displeji velmi rychle budou měnit hodnoty.
- Při puštění se hodnota zobrazí na displeji a zozsvítí se příslušný počet LEDek.
- Pokud padne šestka, hází program sám ještě jednou a zobrazí např 6+6=12

### Elektronické piano
Pomocí Arduina pieza a alespoň 8 tlačítek vytvořte jedoduché "piano".

- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Budou k dispozici dvě další tlačítka, jejichž stiskem se spustí jedna ze tří přednastavených melodií.

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

### Teploměr a vlhkoměr
Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.

### Hra na postřeh
Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se v náhodném intervalu rozsvítí LEDka
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na displeji zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Řízení akvária
Připravte program pro Arduino, který bude spínat osvětlení akvária podle nastaveného času. Dále bude měřit a na displeji zobrazovat teplotu v akváriu.
