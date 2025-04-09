# Samostatný projekt
Program a zapojení s Arduinem a alespoň dvěma periferiemi (motory, displeje, čidla, ...).
Projekt budete vypracovávat jak ve škole na hodinách praxe (vždy cca 1 hodinu), tak doma. Projekt musíte odevzdat a odprezentovat do konce tohoto bloku praxe. 
Projekt mi můžete před odesláním poslat k připomínkování, není to povinné, ale můžete si pak do odevzdání opravit chyby.

### Termín odevzdání je úterý 10.6. do 23:59. Odevzdání po termínu znamená snížení známky o jeden stupeň.

## Hodnocení
- Jedna známka za samotný program
    - funkčnost
    - splnění všech bodů zadání
    - včasné odevzdání
    - **prokázání, že kódu rozumíte a pouze jste jej bez pochopení nezkopírovali**
    
- Druhá známka za dokumentaci a prezentaci projektu - **pdf** dokument pojmenovaný **Jmeno_Prijmeni_trida.pdf** [dle šablony](/prezentace/Praxe_projekt_vzor.pdf) obsahující:
    - zadání
    - popis řešení (několik vět svými slovy o tom, jak jste postupovali při řešení, zda jste vybírali z více variant řešení, jaké nástroje/knihovny jste použili,...)
    - schéma (můžete použít např. online nástroj [wokwi.com](https://wokwi.com/projects/new/arduino-uno))
    - fotografii zapojení
    - kód (přehledně naformátovaný a opatřený komentáři)
    - seznam použitých zdrojů včetně knihoven
    - závěr (několik vět svými slovy o tom, zda jste splnili všechny body zadání, jaké problémy jste řešili atd.)
    - svůj projekt na hodině krátce představíte (do 5min). Pokud chcete, můžete si nachystat prezentaci, ale postačí i jen využít odevzdaný pdf dokument.

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
- Nápojový automat na RFID karty (RFID čtečka, displej, klávesnice, servo)+
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
| **Arduino Nano**            | ![image](https://github.com/user-attachments/assets/a0d4935d-25f5-4c34-b37f-c15b99fd0de5)        | Deska se stejným procesorem jako Arduino UNO, které používáme na cvičeních, menší rozmě, dá se zapojit přímo do nepájivého pole |
| **Arduino MEGA**            | ![image](https://github.com/user-attachments/assets/dfc68c81-4204-4c18-a1e6-f4638a4aeb8a)        | Deska s ATmega 2560 (stejný jako používáme v MIT) s 56 IO piny, 16 analogovými vstupy  |
| **Arduino Nano 33 IoT**     | ![image](https://github.com/user-attachments/assets/786927d7-a9dd-4b7f-a89b-2dadaec56278)        | Arduino s výkonnějším procesorem, Bluetooth a WiFi modulem                             |
| **RTC modul**               | ![image](https://github.com/user-attachments/assets/9adb2038-1ba2-457f-baee-32b699a0cb4c)        | Modul reálného času s bateriovým zálohováním, komunikace přes I2C.                     |
| **Datalogger shield**       | ![image](https://github.com/user-attachments/assets/5f35e26e-2472-4b9e-89f0-07c8c61d907c)        | Shield s RTC modulem a SD kartou, vhodný pro ukládání naměřených dat                   |
| **Piezzo bzučák**           | ![image](https://github.com/user-attachments/assets/915a154c-2437-498b-b360-782f329b54b0)        | Pro jednoduché zvukové efekty (pípání, tóny,...)                                       |
| **Fotorezistor**            | ![image](https://github.com/user-attachments/assets/57229505-4e4a-4947-8ad7-ceed27a86a5b)        | Součástka s odporem závislým na osvětlení                                              |
| **Senzor DHT-10**           | ![image](https://github.com/user-attachments/assets/35651040-5b12-45d1-b351-469374d36977)        | Senzor pro měření teploty a vlhkosti                                                   |
| **Bluetooth modul HC-05**   | ![image](https://github.com/user-attachments/assets/5efbe6b5-2384-48c9-8fb8-18d609b244aa)        | Bezdrátový modul pro sériovou komunikaci přes Bluetooth.                               |
| **Senzor HC-SR04**          | ![image](https://github.com/user-attachments/assets/28d46ed1-19c9-4963-9539-1507a4778653)        | Ultrazvukový senzor vzdálenosti rozsah 2cm - 3m                                        |
| **Joystick shield**         | ![image](https://github.com/user-attachments/assets/846f1cbd-9d8c-4cbc-9f25-cf07cc208c24)        | Rozšiřující deska s joystickem a několika tlačítky pro ovládání projektů.              |
| **RFID sada**               | ![image](https://github.com/user-attachments/assets/18e01a5d-d6fa-4ce4-baf8-5643684a0bbf)        | Modul pro čtení RFID karet a čipů s frekvencí 13.56 MHz.                               |
| **LCD displej**             | ![image](https://github.com/user-attachments/assets/f4f11759-0de7-4584-8c27-df3feec07481)        | Znakový LCD displej 16x2 pro zobrazení textových informací.                            |
| **OLED displej**            | ![image](https://github.com/user-attachments/assets/5f3feb45-f8dd-4a34-b154-d15ea7ddebbc)        | Malý grafický displej s vysokým kontrastem, komunikace přes I2C                        |
| **Klávesnice**              | ![image](https://github.com/user-attachments/assets/44a55e49-8228-4338-b892-ba8b03b8bc3b)        | Membránová klávesnice 4x4                                                              |
| **Školní robot**            | ![image](https://github.com/user-attachments/assets/d504eca5-61b3-4e1d-9c69-c97d469868f1)        | Robot s Arduinem, motory, ultrazvukovým senzorem a senzory čáry                        |
| **DC motor s kolem**        |![image](https://github.com/user-attachments/assets/12e4e6b4-a12c-49b0-9d16-295ab26846ae)         | Stejnosměrný motor s převodovkou a kolem, vhodný pro stavbu vlastního robota           |
| **Servo**                   | ![image](https://github.com/user-attachments/assets/cc43b452-5f89-42c7-b5ea-1453c391aade)        | Malý servomotor s přesným řízením polohy 0-180°                                        |
| **Krokový motor s řadičem** | ![image](https://github.com/user-attachments/assets/ce0ec819-3d65-4164-b5d5-1739c47b3e6a)        | Motor s přesným krokovým řízením, používaný např. v CNC nebo 3D tisku.                 |
