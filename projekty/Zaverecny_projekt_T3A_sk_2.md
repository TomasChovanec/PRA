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
- jedno Arduino v sesterně, 5 tlačítek připojených kabelem u jednotlivých „postelí“ na pokojích (jeden dvoulůžkový, jeden třílůžkový pokoj)
- Po stisku tlačítka:
  - rozsvítí se LED v sesterně
  - na OLED displeji se zobrazí číslo pokoje a postele
  - pravidelně jednou za 3 sekundy zazní zvukový signál
  - odešle se ID pokoje a postele přes UART do centrální jednotky  
- Vypnutí aktuální signalizace pomocí tlačítka sestry
- Pokud zrovna není alarm aktivní, na displeji se bude zobrazovat počet volání z jednotlivých pokojů v posledních dvou hodinách


## 2. Monitor teploty pacienta
- Měření teploty pomocí teplotního čidla  
- OLED displej zobrazuje:
  - aktuální teplotu
  - trend znázorněný šipkou (klesá/stoupá/je stabilní)  
  - graf vývoje teploty za posledních 20 minut  
  - stav pacienta (OK / horečka – např. formou ikony)
- Umožní z řídící jednotky přes UART nastavit limitní teplotu
- Při překročení limitní teploty odešle alarm přes UART  


## 3. RFID přístup do místnosti
- Identifikace personálu pomocí RFID karty  
- Při platné kartě:
  - otevření dveří (servo motor)  
- Při neplatné kartě:
  - zobrazení chyby na displeji
- Všechny pokusy o přstup odesílá včetně časové značky do řídící jednotky
- Evidence vstupů včetně času ukládaná na SD kartu  


## 4. Osvětlení pokoje (Bluetooth)
- Využití LDR senzoru pro detekci okolního světla  
- Automatické zapnutí/vypnutí osvětlení podle intenzity světla  
- Plynulé stmívání a rozsvěcení pomocí PWM  
- Možnost manuálního ovládání (override) přes Bluetooth  

## 5. Transport jídla (robot)
- Robot sledující čáru (line follower)  
- Po příjezdu na stanici (na konec černé čáry):
  - zastaví  
  - čeká na stisk tlačítka (potvrzení převzetí)  
- Po potvrzení se vrací se zpět  
- Evidence počtu jízd (zobrazení na displeji)  

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


## 7. Řídící jednotka včetně webového rozhraní
- Přijímá data z jednotky pro přivolání sestry a z jednotky monitoringu teploty
- Zobrazení stavu systému:
  - webové rozhraní  
- Umožňuje nastavovat limitní teplotu monitorovací jednotky přes webové rozhraní

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
