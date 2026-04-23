# Závěrečný projekt

## Zadání
Jste vývojová firma, která získala zakázku na návrh a realizaci IoT řešení pro hudební festival.  
Vaším úkolem je navrhnout a implementovat jednotlivé subsystémy a zajistit jejich vzájemnou komunikaci.

## Průběžné reporty projektu
Každá dvojice je povinna jednou za 14 dní (vždy nejpozději před začátkem hodiny PRA) sdílet průběžný stav projektu v Teams skupině. Report bude hodnocen známkou s vahou 0,25.

### Obsah reportu
Report by měl mít formu stručné zprávy v Teams skupině. Musí obsahovat:
1. Co se podařilo realizovat
2. Na jaké problémy jste narazili (co nefunguje)
3. Jaké jsou další kroky / co plánujete řešit
4. Součástí každého reportu musí být alespoň jedna z následujících položek:
- fotografie zapojení
- krátké video (max. 1 minuta)
- ukázka zdrojového kódu


## 1. Turnikety Daniel F., Dominik K. :heavy_check_mark:
- Vstupní systém tvořený dvěma turnikety  
- Každý turniket využívá dvojici IR senzorů (detekce směru průchodu)  
- Počítání návštěvníků (příchod / odchod)  
- Při změně počtu odešle aktuální stav přes UART do centrální jednotky
- 2× OLED displej:
  - při příchodu zobrazí „Welcome“
  - při odchodu zobrazí „Good bye“
  - zobrazení realizujte formou bitmapy
 
- HW: Nano, 2xOLED, 4xIR senzor, velké pole

## 2. Výčep Dominik G., Marek H.
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


## 3. Robot pro rozvoz nápojů - Richard.F., Jakub.K. :heavy_check_mark:
- Pohyb po čáře (line follower)
- Po příjezdu na místo:
  - čeká na stisk tlačítka (potvrzení převzetí)
- Následně se vrátí zpět na výchozí pozici
- Na displeji zobrazuje počet jízd
- HW: Robot, OLED displej, USB-C kabel


## 4. Platební terminál k jukeboxu - Vít.K., Adam.H. :heavy_check_mark:
- Načítání dat z RFID karty
- Přes Bluetooth přijme od jukeboxu požadavek na platbu včetně částky
- Pokud je na kartě dostatečný zůstatek, odečte kredit z karty (kredit je opravdu uložen na kartě, nikoli v terminálu!)
- Na displeji zobrazí potvrzení popř. chybu
- Odeslání potvrzení o úspěšné platbě:
  - potvrzovací zpráva musí být pokaždé odlišná
  - cílem je zabránit jednoduchému podvržení komunikace
- HW: UNO, RFID modul, 2 karty, OLED displej, AB kabel, velké nepájivé pole


## 5. Jukebox Jakub K., Josef K.  :heavy_check_mark: 
- Obsahuje minimálně 10 skladeb
- Umožní uživateli vybrat název skladby pomocí displeje a joysticku
- Přijímá platby z platebního terminálu
- Po zaplacení přehraje skladbu
- Ověřuje potvrzovací zprávu:
  - zpráva je pokaždé jiná
  - navrhněte a implementujte vhodný algoritmus ve spolupráci s týmem, který vyvíjí platební terminál
- HW: OLED displej, reproduktor, joystic, mp3 modul, sd karta, čtečka sd karet, pole, kabel mini

## 6. Automatické osvětlení areálu Matouš G., Max F.
- Využívá LDR (světelný senzor)
- Funkce:
  - zapíná osvětlení při tmě
  - vypíná při dostatečném osvětlení
- Implementujte hysterezi
- Plynulé stmívání/rozsvěcení (PWM, cca 10 s)
- Umožňuje barvy přes UART, např.: "R:50 G:255 B:215\n"
- Každých 30 s odesílá přes UART do centrální jednotky aktuální teplotu
- HW: LDR, RGB ledka, DHT11, nano, malé pole


## 7. Centrální jednotka a webový dashboard pro organizátory Petr.K., Matouš K. :heavy_check_mark:
- Hardware:
- Arduino MEGA
- Arduino Nano IoT
- Funkce:
- přijímá data z:
  - turniketů
  - výčepu
  - osvětlení
- zobrazuje data na webové stránce
- umožňuje barvy osvětlení areálu pomocí ovládacích prvků na webu
- HW: Arduino MEGA, Arduino Nano IoT

## 8. Zabezpečovací systém objektu v areálu festivalu – Daniel L.
- Systém využívá 4× PIR senzor (4 místnosti) 
  - při detekci pohybu vyhodnocuje narušení objektu  

- Ovládání pomocí klávesnice:
  - zadání PIN kódu pro odemknutí (deaktivaci alarmu)
  - systém umožňuje změnu PIN kódu:
  - změna dostupná pouze po zadání správného aktuálního PINu
  - nový PIN musí mít definovanou délku (např. 4 číslice)
  - zobrazuje aktuální stav systému na OLED displeji

- Alarm:
  - při narušení objektu (aktivní systém + detekce PIR):
    - akustická signalizace (bzučák)
    - optická signalizace (LED)

- UART komunikace:
  - odesílá logy **včetně času** do centrální jednotky:
    - aktivace / deaktivace systému
    - úspěšné / neúspěšné zadání PINu
    - detekce pohybu (včetně identifikace senzoru)
    - změna PINu


## Hodnocení
- Dvě známky s vahou 0,25 za průběžné reporty projektu
- Jedna známka s váhou 1.0 za samotný projekt (fyzické zapojení a program) a jeho prezentaci
    - **Funkčnost**, splnění všech bodů zadání
    - **Znalost toho, jak program funguje** (prokázání, že kódu rozumíte a pouze jste jej bez pochopení nezkopírovali)
    - **Včasné odevzdání** 
    - **Prezentace** před třídou včetně předvedení funkčnosti (2min prezentace plus čas na dotazy. Vhodné je během prezentace buďto promítnout fotky/video projektu nebo projekt předvést na živo)
    
- Druhá známka s váhou 1.0 za dokumentaci projektu
    - **pdf** dokument pojmenovaný **Prijmeni1_Prijmeni2_trida.pdf** [dle šablony](../files/Praxe_projekt_vzor.pdf) (1 bod) obsahující:
        - **Zadání** - kompletní zadání zkopírované z Githubu
        - **Popis řešení** - několik vět svými slovy o tom, jak jste postupovali při řešení, zda jste vybírali z více variant řešení, jaké nástroje/knihovny jste použili,...)
        - **Schéma** - můžete použít libovolný program pro kreslení schémat nebo např. online nástroj [wokwi.com](https://wokwi.com/projects/new/arduino-uno) nebo KiCAD či jiný SW pro kreslení schemat. Podstatné je, aby bylo možné podle schematu váš projekt znovu vytvořit někým jiným. 
        - **Včasné odevzdání** 
        - **Fotografii** zapojení
        - **Kód** - přehledně naformátovaný a opatřený komentáři, vložený jako text, nikoli jako obrázek
        - **Seznam použitých zdrojů** včetně odkazů na použité knihovny
        - **Závěr** - několik vět svými slovy o tom, zda jste splnili všechny body zadání, jaké problémy jste řešili atd.
        - **Celková úprava dokumentu** - zarovnání písma do bloku, použití vhodného písma, žádné osamocené nadpisy na konci stránky
