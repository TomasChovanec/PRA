## Zadání projektů E3A

Níže najdete detailní zadání projektu. V odůvodněných případech lze zadání po ústní nebo mailové dohodě změnit. 


### Jan Sliž - Elektronická kostka
Pomocí Arduina, displeje a  tlačítka vytvořte elektronickou hrací kostku.
- Po stisku se na displeji velmi rychle budou měnit hodnoty. 
 - Při puštění se hodnota zobrazí
 - Pokud padne šestka, hází program sám ještě jednou a zobrazí např 6+6=12


### Dominik Slovák, Martin Ščepka, Matěj Šedivý - Robot Line follower

Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)

### Jan Svoboda - Parkovací čidlo

Pomocí Arduina, pieza a ultarzvukového senzoru vytvořte parkovací senzor pro auto
- Senzor je aktivní pouze když je stisknuto tlačítko (simulujeme spínač na zpátečce v autě)
- Když je překážka vzdálena více než 100 cm, bzučák nebude vydávat žádný zvuk.
- Pokud se překážka nachází mezi 100 cm a 50 cm, bzučák vydá krátký zvuk jednou za sekundu.
- Když se překážka přiblíží na 50–20 cm, pípání bude jednou za půl sekundy.
- Pokud je překážka blíže než 20 cm, bzučák bude pípat neustále.

### Tadeáš Svobodník - Piano
Pomocí Arduina pieza a alespoň 4 tlačítek vytvořte jedoduché "piano". 
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Po stisku dvou tlačítek současně se přehraje přednastavená melodie.


### Adam Vodrážka - Elektronický zámek
Pomocí Arduina vytvořte elektronický zámek s klávesnicí, displejem a servem
- Zámek se bude otevírat čtyřmístným číselným kódem potvrzeným křížkem
- Po 3 chybných zadáních se zámek na 10s zablokuje (odpočet bude na displeji)
- Projekt bude umožňovat změnu kódu bez změny programu (bez nutnosti nahrát znovu kód do arduina)

### Jakub Vašek - Automatické otevírání kurníku
Pomocí Arduina, fotorezistoru a krokového motoru vytvořte automatické ovládání vrátek do kurníku v závislosti na slunečním svitu.
- Ošetřete například případy, kdy čidlo někdo krátkodobě zakryje rukou, nebo na něj naopak krátkodobě zasvítí např. světlo projíždějícího auta


