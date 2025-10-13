### Elektronické piano (Jakub 6.11.)
Pomocí Arduina pieza a alespoň 5 tlačítek vytvořte jedoduché "piano".
- Po stisku tlačítka se přehraje příslušný tón.
- Kód by měl být napsán tak, aby bylo možné snadno přidat více tlačítek pro další tóny.
- Při stisku dvou tlačítek najednou se spustí předem nastavená melodie


### Hra na postřeh 2 hráče (Ondřej 6.11.)
- Pomocí Arduina vytvořte hru na postřeh pro dva hráče
- Po spuštění hry se postupně rozsítí všechny LED a pak po náhodném intervalu zhasnou
- Každý hráč má své tlačítko, úkolem je stisknout tlačítko co nejdříve po rozsvícení LEDky. Pokud hráč stiskne tlačítko dříve, než se LEDka rozsvítí, prohrál
- Program po každém kole ukáže, který hráč vyhrál a o kolik sekund
- Po pěti kolech se na serial monitoru zobrazí celkové skóre, vítěz a suma času, o kolik byl rychlejší

### Regulace ventilátoru (Jiří 6.11.)
- Pomocí teplotního čidla a Arduina ovládejte otáčky ventilátoru v závislosti na aktuální teplotě.
- Pod 25 °C: ventilátor vypnutý
- 25–30 °C: 30–60 % výkonu
- Nad 30 °C: 100 % výkonu a přerušovaný zvukový signál
- Aktuální hodnotu teploty a PWM zobrazujte na LCD displeji

### Elektronická kostka (Sebastian 13.11.)
- Pomocí Arduina, LED diod a  tlačítka vytvořte elektronickou hrací kostku.
- Při stisku (a držení) tlačítka se na LEDkách budou velmi rychle měnit náhodné hodnoty. 
- Po puštění tlačítka se hodnota zastaví


### Hodiny, stopky (Milan 13.11.)
- Pomocí Arduina, LCD displeje a tlačítek vytvořte hodiny se stopkami a budíkem
- Jedním tlačítkem se bude měnit aktálně zobrazovaná funkce (hodiny/stopky/nastavení budíku)
- Druhé tlačítko bude mít u stopek funkci start/stop, u budíku zvýšení minut u času buzení
- Třetí tlačítko bude mít u stopek funkci reset, u budíku zvýšení hodin v čase buzení

  
### Robot Line follower (Dan 13.11.)
Vytvořte program pro školního Arduino robota, který bude fungovat jako sledovač čáry.
- Robot bude detekovat černou čáru optickými čidly a pojede po ní
- Optimalizujte program robota na co nejrychlejší projetí trati
- Pomocí ultrazvukového čidla implementujte zastavení před překážkou
- Po resetu Arduina musí být robot v bezpečném stavu (motory zastaveny), rozjede se až po stisknutí startovacího tlačítka (mikrospínač na robotovi, nikoli vypínač napájení)


