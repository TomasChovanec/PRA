# Závěrečný projekt

## Zadání
Jste vývojová firma, která získala zakázku na návrh a realizaci IoT řešení pro chytrou nemocnici.  
Vaším úkolem je navrhnout a implementovat jednotlivé subsystémy a zajistit jejich vzájemnou komunikaci.

## Průběžné reporty projektu
Každá dvojice je povinna jednou za 14 dní (vždy nejpozději před začátkem hodiny PRA) sdílet průběžný stav projektu v Teams skupině. Report bude hodnocen známkou s vahou 0,25.

### Obsah reportu
Každý report musí obsahovat:
1. Co se podařilo realizovat  
2. Na jaké problémy jste narazili (co nefunguje)  
3. Jaké jsou další kroky / co plánujete řešit  
4. Součástí každého reportu musí být alespoň jedna z následujících položek:
   - fotografie zapojení  
   - krátké video (max. 1 minuta)  
   - ukázka zdrojového kódu  


## 1. Přivolání sestry
- Tlačítka u jednotlivých „postelí“  
- Po stisku tlačítka:
  - rozsvítí se LED (signalizace čekání na sestru)  
  - odešle ID pokoje přes UART do centrální jednotky  
- Reset signalizace pomocí tlačítka sestry  
- Evidence počtu volání pro jednotlivé pokoje  
- HW: Arduino (dle výběru), tlačítka, LED, nepájivé pole  


## 2. Monitor teploty pacienta
- Měření teploty pomocí teplotního čidla  
- OLED displej zobrazuje:
  - aktuální teplotu  
  - graf vývoje teploty za posledních 20 minut  
  - stav pacienta (OK / horečka – např. formou ikony)  
- Při překročení limitní teploty odešle alarm přes UART  
- HW: Arduino, teplotní čidlo, OLED displej  


## 3. RFID přístup do místnosti
- Identifikace personálu pomocí RFID karty  
- Při platné kartě:
  - otevření dveří (servo motor)  
- Při neplatné kartě:
  - zobrazení chyby na displeji  
- Evidence vstupů ukládaná na SD kartu  
- HW: Arduino, RFID modul, servo, SD karta, displej  


## 4. Osvětlení pokoje (Bluetooth)
- Využití LDR senzoru pro detekci okolního světla  
- Automatické zapnutí/vypnutí osvětlení podle intenzity světla  
- Plynulé stmívání a rozsvěcení pomocí PWM  
- Možnost manuálního ovládání (override) přes Bluetooth  
- HW: Arduino, LDR, LED (nebo RGB LED), Bluetooth modul  

## 5. Transport jídla (robot)
- Robot sledující čáru (line follower)  
- Po příjezdu na stanici:
  - zastaví  
  - čeká na stisk tlačítka (potvrzení převzetí)  
- Po potvrzení pokračuje / vrací se zpět  
- Evidence počtu jízd (zobrazení na displeji)  
- HW: robotická platforma, senzory čáry, tlačítko, displej  

## 6. Nákladní výtah
- Simulace výtahu pomocí krokového motoru  
- Ovládání pomocí klávesnice (volba patra)  
- OLED displej:
  - po stisku tlačítka zobrazí na 2 s instrukci k nástupu  
- Následně:
  - krokový motor se roztočí  
  - směr otáčení odpovídá směru jízdy (nahoru / dolů)  
  - jedno patro = jedna otáčka motoru  
- Během jízdy:
  - zobrazení aktuální polohy výtahu  
  - indikace směru (šipka nahoru / dolů)  
- Pokud během jízdy přijde nový požadavek:
  - výtah nejprve dokončí aktuální jízdu  
  - poté obslouží nový požadavek  
- HW: Arduino, krokový motor, driver, OLED displej, klávesnice  


## 7. Supervizor systému (webové rozhraní)
- Centrální jednotka sleduje ostatní moduly  
- Přijímá data ze všech zařízení přes UART  
- Pokud některý modul nekomunikuje:
  - vyhlásí chybu (watchdog logika)  
- Zobrazení stavu systému:
  - webové rozhraní  
  - OLED displej (základní stav systému)  
- HW: Arduino MEGA / IoT deska, OLED displej  

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
