## Zadání projektů E3B skupina 3

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit.


### Ovládání robota pomocí gamepadu pro Playstation (J.H.)
 - Upravte školního robota tak, aby motory byly řízeny deskou s procesorem ESP32
 - Naprogramujte robota tak, aby jej bylo možné ovládat gamepadem přes Bluetooth.


### Elektronická hrací kostka (T.H., V.H.)
- Pomocí Arduina, tlačítka a 6 LEDek vytvořte elektronickou kostku.
- Po stisknutí tlačítka se kostka "hodí" a po puštění zobrazí výsledek pomocí LED.
- Při hodnotě 6 se hází automaticky ještě jednou a výsledek se ukáže postupně.


### Voltmetr (M.B.)
- Pomocí Arduina vytvořte multimetr
- Alespoň dva napěťové rozsahy
- Měření proudu pomocí obvodu INA219


### Otvírání dveří dle slunce (J.D.)
- Pomocí Arduina, fotorezistoru a krokového motoru vytvořte automatické ovládání vrátek do kurníku v závislosti na slunečním svitu.
- Ošetřete například případy, kdy čidlo někdo krátkodobě zakryje rukou, nebo na něj naopak krátkodobě zasvítí např. světlo projíždějícího auta


### Automatické ovládání brány (J.G., J.B.)
- Vytvořte program a zrealizujte zapojení pro Arduino, které automaticky otevře bránu, když k ní přijede auto a po projetí ji opět zavře. Požadované funkce:
- Dokud není detekováno auto, brána je zavřená.
- Po detekci auta se brána otevře.
- Dokud auto stojí před branou, brána zůstává otevřená. Teprve až auto projede, brána se zavře.
- Pokud by ale auto neprojelo do 30s, brána se zavře.
- Jako bezpečnostní prvek, aby nedošlo ke zranění případných chodců, před započetím pohybu (otvírání nebo zavírání) 5x blikne červené výstražné světlo a 5x zazní varovný zvukový signál.


### Hodinky se stopkami a budíkem (O.E.)
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení


### Ultrazvukový senzor vzdálenosti s výpočtem plochy (M.B.)
- Pomocí ultrazvukového senzoru HC-SR04, Arduina a tlačítek vytvořte zařízení, které změří délku a šířku objektu a vypočítá plochu.
- Měřená hodnota se průběžne zobrazuje na displeji, stiskem tlačítka se potvrdí a přejde se na měření další hodnoty
- Po zadání všech hodnot se zobrazí všechny naměřené hodnoty spolu s výslednou plochou


### Regulace ventilátoru (D.G.)
- Pomocí teplotního čidla a Arduina ovládejte otáčky ventilátoru v závislosti na aktuální teplotě.
- Pod 25 °C: ventilátor vypnutý
- 25–30 °C: 30–60 % výkonu
- Nad 30 °C: 100 % výkonu
- Aktuální hodnotu teploty a PWM posílejte na Serial monitor
