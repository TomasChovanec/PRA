# Samostatný projekt
Program a zapojení s Arduinem a alespoň dvěma periferiemi (motory, displeje, čidla, ...).
Projekt budete vypracovávat jak ve škole na hodinách praxe (vždy cca 1 hodinu), tak doma. Projekt musíte odevzdat a odprezentovat do konce tohoto bloku praxe. 
Projekt mi můžete před odesláním poslat k připomínkování, není to povinné, ale můžete si pak do odevzdání opravit chyby.

### Termín odevzdání je úterý 10.6. do 23:59. Odevzdání po termínu znamená snížení známky o jeden stupeň.

## Hodnocení
- Jedna známka za samotný program
    - Funkčnost
    - Splnění všech bodů zadání
    - Včasné odevzdání
    - **Prokázání, že kódu rozumíte a pouze jste jej bez pochopení nezkopírovali**
    
- Druhá známka za dokumentaci a prezentaci projektu - **pdf** dokument pojmenovaný **Jmeno_Prijmeni_trida.pdf** [dle šablony](/prezentace/Praxe_projekt_vzor.pdf) obsahující:
    - **Zadání** - kompletní zadání zkopírované z githubu
    - **Popis řešení** - několik vět svými slovy o tom, jak jste postupovali při řešení, zda jste vybírali z více variant řešení, jaké nástroje/knihovny jste použili,...)
    - **Schéma** - můžete použít např. online nástroj [wokwi.com](https://wokwi.com/projects/new/arduino-uno))
    - **Fotografii** zapojení
    - **Kód** - přehledně naformátovaný a opatřený komentáři
    - **Seznam použitých zdrojů** včetně knihoven
    - **Závěr** - několik vět svými slovy o tom, zda jste splnili všechny body zadání, jaké problémy jste řešili atd.
    - Svůj projekt na hodině krátce představíte (do 5min). Pokud chcete, můžete si nachystat prezentaci, ale postačí i jen využít odevzdaný pdf dokument.

## Příklady možných projektů (ale vítané jsou vlastní nápady):
- Elektronická hrací kostka
- Elektronické piano
- Ultrazvukový měřič vzdálenosti s funkcí výpočtu plochy
- Automatické otvírání dveří se servem a ultrazvukovým čidlem
- Hra na postřeh pro dva hráče
- Hodinky, budík a stopky
- Teplotní čidlo se záznamem na SD kartu
- Voltmetr
- Ovládání výtahu (krokový motor, tlačítka, displej)
- Otevírání dveří na RFID karty (RFID čtečka, displej, servo)
- Nápojový automat na RFID karty (RFID čtečka, displej, klávesnice, servo)
- Hračka s mp3 modulem
- Reklamní banner s maticovým displejem
- Naprogramování školního robota jako sledovače čáry s funkcí objetí překážky
- Stavba robota podle vlastního návrhu


<!---
- Přidání funkce počitadla ujeté vzdálenosti pro robota
- Naprogramování školního robota pro soutěž sumo 
- Časomíra pro závody robotů
- Úprava školního robota pro ovládání joystickem po drátech
--->

## Moduly a součástky pro projekt

Můžete si pro potřeby projektu zapůjčit následující vybavení:


| Komponenta                  | Obrázek                                                                                          | Popis                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Arduino Nano**            | ![image](img/Projekt_1.png)        | Deska se stejným procesorem jako Arduino UNO, které používáme na cvičeních, menší rozměry, dá se zapojit přímo do nepájivého pole |
| **Arduino MEGA**            | ![image](img/Projekt_2.png)        | Deska s ATmega 2560 (stejný jako používáme v MIT) s 56 IO piny, 16 analogovými vstupy  |
| **Arduino Nano 33 IoT**     | ![image](img/Projekt_3.png)        | Arduino s výkonnějším procesorem, Bluetooth a WiFi modulem                             |
| **RTC modul**               | ![image](img/Projekt_4.png)        | Modul reálného času s bateriovým zálohováním, komunikace přes I2C.                     |
| **Datalogger shield**       | ![image](img/Projekt_5.png)        | Shield s RTC modulem a SD kartou, vhodný pro ukládání naměřených dat                   |
| **Piezzo bzučák**           | ![image](img/Projekt_6.png)        | Pro jednoduché zvukové efekty (pípání, tóny,...)                                       |
| **Fotorezistor**            | ![image](img/Projekt_7.png)        | Součástka s odporem závislým na osvětlení                                              |
| **Senzor DHT-10**           | ![image](img/Projekt_8.png)        | Senzor pro měření teploty a vlhkosti                                                   |
| **Bluetooth modul HC-05**   | ![image](img/Projekt_9.png)        | Bezdrátový modul pro sériovou komunikaci přes Bluetooth.                               |
| **Senzor HC-SR04**          | ![image](img/Projekt_10.png)        | Ultrazvukový senzor vzdálenosti rozsah 2cm - 3m                                        |
| **Joystick shield**         | ![image](img/Projekt_11.png)        | Rozšiřující deska s joystickem a několika tlačítky pro ovládání projektů.              |
| **RFID sada**               | ![image](img/Projekt_12.png)        | Modul pro čtení RFID karet a čipů s frekvencí 13.56 MHz.                               |
| **LCD displej**             | ![image](img/Projekt_13.png)        | Znakový LCD displej 16x2 pro zobrazení textových informací.                            |
| **OLED displej**            | ![image](img/Projekt_14.png)        | Malý grafický displej s vysokým kontrastem, komunikace přes I2C                        |
| **Klávesnice**              | ![image](img/Projekt_15.png)        | Membránová klávesnice 4x4                                                              |
| **Školní robot**            | ![image](img/Projekt_16.png)        | Robot s Arduinem, motory, ultrazvukovým senzorem a senzory čáry                        |
| **DC motor s kolem**        | ![image](img/Projekt_17.png)        | Stejnosměrný motor s převodovkou a kolem, vhodný pro stavbu vlastního robota           |
| **Servo**                   | ![image](img/Projekt_18.png)        | Malý servomotor s přesným řízením polohy 0-180°                                        |
| **Krokový motor s řadičem** | ![image](img/Projekt_19.png)        | Motor s přesným krokovým řízením, používaný např. v CNC nebo 3D tisku.                 |
| **Hmotnostní senzor**       | ![image](img/Projekt_20.png)        | Hmotnostní senzor s modulem HX711 (24bit ADC)    do 5kg nebo do 20kg                   |
| **Senzor srdečního tepu**   | ![image](img/Projekt_21.png)        | Senzor srdečního tepu s modulem MAX30100                                               |
| **Modul s MP3 přehrávačem** | ![image](img/Projekt_22.png)        | Modul s MP3 přehrávačem a integrovaným zesilovačem, který může být připojen přímo k reproduktoru. |
| **Maticový displej**        | ![image](img/Projekt_23.png)        | MLED Matrix matice 8x8x4 s MAX7219 - červená                                           |
| **GPS modul**               | ![image](img/Projekt_24.png)        | Modul GPS NEO-6M s anténou                                                             |
| **Ventilátor**              | ![image](img/Projekt_25.png)        | Ventilátor 50mm 5V                                                                     |
| **Senzor proudu**           | ![image](img/Projekt_26.png)        | Senzor INA219 pro měření proudu. Připojení pře I2C                                     |
| **Akcelerometr**            | ![image](img/Projekt_27.png)        | Tříosý akcelerometr GY 521                                                             |
| **Kruh z RGB LEDek**        | ![image](img/Projekt_28.png)        | 24x RGB LED WS2812B                                                                    |






