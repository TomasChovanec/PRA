# Závěrečný projekt – PRA

## Zadání
Jste vývojová firma, která získala zakázku na návrh a realizaci IoT řešení pro hudební festival.  
Vaším úkolem je navrhnout a implementovat jednotlivé subsystémy a zajistit jejich vzájemnou komunikaci.

## Průběžné reporty projektu
Každá dvojice je povinna jednou za 14 dní (vždy nejpozději před začátkem hodiny PRA) sdílet průběžný stav projektu v Teams skupině. Report bude hodnocen známkou s vahou 0,25.

### Obsah reportu
Každý report musí obsahovat:
1. Co se podařilo realizovat
2. Na jaké problémy jste narazili (co nefunguje)
3. Jaké jsou další kroky / co plánujete řešit

### Povinné přílohy
Součástí každého reportu musí být alespoň jedna z následujících položek:
- fotografie zapojení
- krátké video (max. 1 minuta)
- ukázka zdrojového kódu


## 1. Turnikety
- Vstupní systém tvořený dvěma turnikety  
- Každý turniket využívá dvojici IR senzorů (detekce směru průchodu)  
- Počítání návštěvníků (příchod / odchod)  
- Při změně počtu odešle aktuální stav přes UART do centrální jednotky
- 2× OLED displej:
  - při příchodu zobrazí „Welcome“
  - při odchodu zobrazí „Good bye“
  - zobrazení realizujte formou bitmapy

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


## 4. Platební terminál k jukeboxu
- Načítání dat z RFID karty
- Přes Bluetooth přijme od jukeboxu požadavek na platbu včetně částky
- Pokud je na kartě dostatečný zůstatek, odečte kredit z karty (kredit je opravdu uložen na kartě, nikoli v terminálu!)
- Odeslání potvrzení o úspěšné platbě:
  - potvrzovací zpráva musí být pokaždé odlišná
  - cílem je zabránit jednoduchému podvržení komunikace


## 5. Jukebox
- Obsahuje minimálně 10 skladeb
- Přijímá platby z platebního terminálu
- Ověřuje potvrzovací zprávu:
  - zpráva je pokaždé jiná
  - navrhněte a implementujte vhodný algoritmus ve spolupráci s týmem, který vyvíjí platební terminál


## 6. Automatické osvětlení areálu
- Využívá LDR (světelný senzor)
- Funkce:
  - zapíná osvětlení při tmě
  - vypíná při dostatečném osvětlení
- Implementujte hysterezi
- Plynulé stmívání/rozsvěcení (PWM, cca 10 s)
- Umožňuje barvy přes UART, např.: "R:50 G:255 B:215\n"
- Každých 30 s odesílá přes UART do centrální jednotky aktuální teplotu


## 7. Centrální jednotka a webový dashboard pro organizátory
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
