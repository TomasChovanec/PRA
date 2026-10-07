# Závěrečný projekt

## Zadání

Jste vývojová firma, která získala zakázku na návrh a realizaci IoT řešení pro hudební festival.
Vaším úkolem je navrhnout a implementovat jednotlivé subsystémy a zajistit jejich vzájemnou komunikaci.

## Odevzdání

- Odevzdání dokumentace mailem do ?????
- Prezentace ve škole ?????

## Průběžné reporty projektu

???? Report bude hodnocen známkou s vahou 0,25.

## 1. Turnikety

- Vstupní systém tvořený dvěma turnikety
- Každý turniket využívá dvojici IR senzorů (detekce směru průchodu)
- Počítání návštěvníků (příchod / odchod)
- Při změně počtu odešle aktuální stav přes UART do centrální jednotky
- 2× OLED displej:
  - při příchodu zobrazí „Welcome“
  - při odchodu zobrazí „Good bye“
  - zobrazení realizujte formou bitmapy

**HW:** Nano, 2× OLED, 4× IR senzor, velké pole

## 2. Výčep

- Ovládání pomocí tlačítek:
  - 3× tlačítko pro malý nápoj
  - 3× tlačítko pro velký nápoj
- Nabídka nápojů:
  - Pivo
  - Birell
  - Kofola
- Po stisknutí tlačítka:
  - servo simuluje otevření ventilu
  - na OLED displeji se zobrazuje průběh plnění v procentech
- Eviduje celkové množství jednotlivých vydaných nápojů (výtoč)
- Sleduje kapacitu sudů:
  - kapacity definujte pomocí konstant/maker na začátku programu
  - při poklesu odešle varování přes UART do centrální jednotky

## 3. Robot pro rozvoz nápojů

- Pohyb po čáře (line follower)
- Po příjezdu na místo:
  - čeká na stisk tlačítka (potvrzení převzetí)
- Následně se vrátí zpět na výchozí pozici
- Na displeji zobrazuje počet jízd

**HW:** Robot, OLED displej, USB-C kabel

## 4. Platební terminál k jukeboxu

- Načítání dat z RFID karty
- Přes Bluetooth přijme od jukeboxu požadavek na platbu včetně částky
- Pokud je na kartě dostatečný zůstatek, odečte kredit z karty (kredit je opravdu uložen na kartě, nikoli v terminálu!)
- Na displeji zobrazí potvrzení popř. chybu
- Odeslání potvrzení o úspěšné platbě:
  - potvrzovací zpráva musí být pokaždé odlišná
  - cílem je zabránit jednoduchému podvržení komunikace

**HW:** UNO, RFID modul, 2 karty, OLED displej, AB kabel, velké nepájivé pole

## 5. Jukebox

- Obsahuje minimálně 10 skladeb
- Umožní uživateli vybrat název skladby pomocí displeje a joysticku
- Přijímá platby z platebního terminálu
- Po zaplacení přehraje skladbu
- Ověřuje potvrzovací zprávu:
  - zpráva je pokaždé jiná
  - navrhněte a implementujte vhodný algoritmus ve spolupráci s týmem, který vyvíjí platební terminál

**HW:** OLED displej, reproduktor, joystick, mp3 modul, SD karta, čtečka SD karet, pole, kabel mini

## 6. Automatické osvětlení areálu

- Využívá LDR (světelný senzor)
- Funkce:
  - zapíná osvětlení při tmě
  - vypíná při dostatečném osvětlení
- Implementujte hysterezi
- Plynulé stmívání/rozsvěcení (PWM, cca 10 s)
- Umožňuje nastavit barvy přes UART, např.: `R:50 G:255 B:215\n`
- Každých 30 s odesílá přes UART do centrální jednotky aktuální teplotu

**HW:** LDR, RGB LED, DHT11, Nano, malé pole

## 7. Chytré odpadkové koše

- Minimálně 3 koše
- Každý koš má senzor zaplnění
- Na displeji se zobrazuje stav:
  - OK
  - HALF
  - FULL
- Při dosažení definované úrovně odešle zařízení upozornění centrální jednotce
- Centrální jednotka zobrazí stav všech košů
- Po vyprázdnění lze koš resetovat tlačítkem

**Rozšíření:**

- Centrální jednotka zobrazí, který koš je potřeba vyprázdnit jako první.

## 8. Festivalová meteostanice

- Měří:
  - teplotu
  - vlhkost
  - intenzitu osvětlení
- Na OLED zobrazuje aktuální hodnoty
- Každých 30 s odesílá naměřená data centrální jednotce
- Centrální jednotka zobrazuje aktuální hodnoty na webu
- Při překročení definovaných hodnot odešle výstrahu

Například:

```
TEMP: 31.4 C
HUM: 68 %
LIGHT: 734
WARNING: HOT
```

**Rozšíření:**

- Vytvořte jednoduchý min/max záznam hodnot.

## 9. Řízení ventilace stanu

- Systém sleduje:
  - teplotu
  - vlhkost
- Podle naměřených hodnot automaticky řídí ventilátor
- Ventilátor má minimálně 3 režimy:
  - vypnuto
  - pomalu
  - rychle
- Řízení rychlosti realizujte pomocí PWM
- Použijte hysterezi, aby ventilátor neustále nepřepínal mezi režimy
- Na OLED zobrazujte:
  - teplotu
  - vlhkost
  - aktuální výkon ventilátoru
- Data odesílejte do centrální jednotky

**HW:** Nano, DHT11/DHT22, ventilátor, tranzistor/MOSFET, OLED

**Rozšíření:**

- Centrální jednotka umožní přepnout mezi automatickým a manuálním režimem.

## 10. Parkovací systém festivalu

- Systém sleduje obsazenost parkovacích míst
- Využívá minimálně 4 parkovací pozice, každá má vlastní senzor
- Při příjezdu vozidla:
  - zjistí první volné místo
  - rozsvítí příslušnou LED
  - na displeji zobrazí počet volných míst
- Při odjezdu se místo opět označí jako volné
- Systém musí rozlišovat:
  - volné místo
  - obsazené místo
- Při úplném obsazení zobrazí „PARKOVIŠTĚ PLNÉ“
- Každá změna obsazenosti je odeslána přes UART do centrální jednotky
- Centrální jednotka zobrazuje počet volných míst na webu

**HW:** Nano, 4× IR senzor, OLED, LED, tlačítko / simulace vozidel

**Rozšíření:**

- Pošlete centrální jednotce také informaci o konkrétním obsazeném místě.

## 11. Centrální jednotka a webový dashboard pro organizátory

- Přijímá data z:
  - turniketů
  - výčepu
  - osvětlení
- Zobrazuje data na webové stránce
- Umožňuje nastavit barvy osvětlení areálu pomocí ovládacích prvků na webu

**HW:** Arduino MEGA, Arduino Nano IoT


## Hodnocení

- Dvě známky s vahou 0,25 za průběžné reporty projektu
- Jedna známka s váhou 1.0 za samotný projekt (fyzické zapojení a program) a jeho prezentaci:
  - **Funkčnost**, splnění všech bodů zadání
  - **Znalost toho, jak program funguje** (prokázání, že kódu rozumíte a pouze jste jej bez pochopení nezkopírovali)
  - **Včasné odevzdání**
  - **Prezentace** před třídou včetně předvedení funkčnosti (2 min prezentace plus čas na dotazy; vhodné je během prezentace buď promítnout fotky/video projektu, nebo projekt předvést naživo)
- Druhá známka s váhou 1.0 za dokumentaci projektu:
  - **PDF** dokument pojmenovaný **Prijmeni1_Prijmeni2_trida.pdf** [dle šablony](../files/Praxe_projekt_vzor.pdf) (1 bod) obsahující:
    - **Zadání** – kompletní zadání zkopírované z GitHubu
    - **Popis řešení** – několik vvět svými slovy o tom, jak jste postupovali při řešení, zda jste vybírali z více variant řešení, jaké nástroje/knihovny jste použili, ...
    - **Schéma** – můžete použít libovolný program pro kreslení schémat, např. online nástroj [wokwi.com](https://wokwi.com/projects/new/arduino-uno), KiCAD či jiný SW. Podstatné je, aby bylo možné podle schématu váš projekt znovu vytvořit někým jiným
    - **Včasné odevzdání**
    - **Fotografii** zapojení
    - **Kód** – přehledně naformátovaný a opatřený komentáři, vložený jako text, nikoli jako obrázek
    - **Seznam použitých zdrojů** včetně odkazů na použité knihovny
    - **Závěr** – několik vět svými slovy o tom, zda jste splnili všechny body zadání, jaké problémy jste řešili atd.
    - **Celková úprava dokumentu** – zarovnání písma do bloku, použití vhodného písma, žádné osamocené nadpisy na konci stránky
