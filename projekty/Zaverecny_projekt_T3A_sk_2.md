# Závěrečný projekt – PRA

## Zadání
Jste vývojová firma, která získala zakázku na návrh a realizaci IoT řešení pro hudební festival.  
Vaším úkolem je navrhnout a implementovat jednotlivé subsystémy a zajistit jejich vzájemnou komunikaci.

---

## 1. Turniket
- Vstupní systém tvořený dvěma turnikety  
- Každý turniket využívá dvojici IR senzorů (detekce směru průchodu)  
- Počítání návštěvníků (příchod / odchod)  
- Při změně počtu odešle aktuální stav přes UART  
- 2× OLED displej:
  - při příchodu zobrazí „Welcome“
  - při odchodu zobrazí „Good bye“
  - zobrazení realizujte formou bitmapy

---

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
- Eviduje celkové množství vydaných nápojů (výtoč)
- Sleduje kapacitu sudů:
  - kapacity definujte pomocí konstant/maker na začátku programu
  - při poklesu odešle varování přes UART

---

## 3. Robot pro rozvoz nápojů
- Pohyb po čáře (line follower)
- Po příjezdu na místo:
  - čeká na stisk tlačítka (potvrzení převzetí)
- Následně se vrátí zpět na výchozí pozici
- Na displeji zobrazuje počet otoček (např. kol nebo motoru)

---

## 4. Platební terminál k jukeboxu
- Načítání dat z RFID karty
- Zadání částky pomocí klávesnice
- Odečtení kreditu z karty
- Odeslání potvrzení o úspěšné platbě:
  - potvrzovací zpráva musí být pokaždé odlišná
  - cílem je zabránit jednoduchému podvržení komunikace

---

## 5. Jukebox
- Obsahuje minimálně 10 skladeb
- Přijímá platby z platebního terminálu
- Ověřuje potvrzovací zprávu:
  - zpráva je pokaždé jiná
  - navrhněte a implementujte vhodný algoritmus ve spolupráci s terminálem

---

## 6. Automatické osvětlení areálu
- Využívá LDR (světelný senzor)
- Funkce:
  - zapíná osvětlení při tmě
  - vypíná při dostatečném osvětlení
- Implementujte hysterezi
- Plynulé stmívání/rozsvěcení (PWM, cca 10 s)
- Nastavení barvy přes UART, např.: "R:50 G:255 B:215\n"

- Každých 30 s odesílá přes UART aktuální teplotu

---

## 7. Webový dashboard pro organizátory
- Hardware:
- Arduino MEGA
- Arduino Nano IoT
- Funkce:
- přijímá data z:
  - turniketů
  - výčepu
  - osvětlení
- zobrazuje data na webové stránce

---

## Požadavky na řešení
- Každý subsystém musí být funkční samostatně
- Komunikace mezi zařízeními probíhá přes UART
- Návrh struktury dat a komunikačního protokolu je součástí projektu
- Důraz na přehlednost kódu a použití vhodné struktury programu
