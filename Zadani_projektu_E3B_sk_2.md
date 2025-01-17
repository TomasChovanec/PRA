## Zadání projektů E3B skupina 2

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 

### Tomáš P. - Nápojový automat na RFID karty
Automat bude obsahovat displej, 4 tlačítka, RFID modul a bzučák.
- Po přiložení karty nebo čipu se na chvíli zobrazí na displeji jméno majitele a zbývající kredit (popř. upozornění na neznámého uživatele)
- Poté se zobrazí nabídka nápojů s cenou
- Uživatel vybere pomocí tlačítek nápoj, pokud má dostatečný kredit nápoj se připraví a vydá
- Příprava nápoje bude simulována zvuky z bzučáku, po dokončení přípravy se ozve krátký vysoký tón
- Cena nápoje se strhne uživateli z kreditu
- Informace o výši kreditu jednotlivých uživatelů musí být zachována i po vypnutí napájení (použijte EEPROM)

### Adam P.
Pomocí Arduina, displeje a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku se na displeji velmi rychle budou měnit hodnoty. 
- Při puštění se hodnota zobrazí
- Pokud padne šestka, hází program sám ještě jednou a zobrazí např 6+6=12

### Jan P. - Elektronické piano
Pomocí Arduina pieza a alespoň 8 tlačítek vytvořte jedoduché "piano".

- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Budou k dispozici dvě další tlačítka, jejichž stiskem se spustí jedna ze tří přednastavených melodií.

### František J., David K. - Ovládání robota přes Bluetooth
Vytvořte program pro školního robota, aby jej bylo možné ovládat přes Bluetooth. Použijte Bluetooth modul HC-05 a robota ovládejte aplikací z telefonu.
- Program bude umožňovat manuální ovládání, kdy se pohyb robota řídí výhradně ovládáním z telefonu
- Dále zde bude autonomní režim, kdy robot bude jezdit rovně a pomocí ultrazvukového čidla detekovat překážky. Když detekuje překážku, otočí se a pojede jinam
- Autonomní a manuální režim bude možné přepínat z telefonu
- Po resetu bude robot v manuálním módu, do autonomního se přepne buď povelem z telefonu nebo stiskem tlačítka na robotovi.

### Nikolas Karoly - Ovládání výtahu
Vytvořte s Arduinem simulaci výtahu. Bude obsahovat krokový motor, servo, displej a tlačítka pro volbu patra.
- Po stisku tlačítka se výtah rozjede, na displeji bude zobrazovat aktuální polohu
- Servo bude simulovat ovládání dveří

  ### Jan N. - Teploměr a vlhkoměr
  Pomocí Arduina vytvořte teploměr a vlhkoměr s měřením na dvou místech - v místnosti a venku. Použijte čidla DHT11, LCD displej pro zobrazení a tlačítko pro přepínání mezi zobrazením hodnot v místnosti a venku.
