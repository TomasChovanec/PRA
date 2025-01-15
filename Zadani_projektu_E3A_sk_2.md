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
