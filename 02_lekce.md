<script type="text/javascript" id="MathJax-script" async 
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"> 
</script> 


## Sériová linka
- Umět posílat data do PC pomocí fuknce Serial.print
- 
## Proměnné

## Podmínky, cykly
- Umět použít [podmínku if-else](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/podminky-a-jejich-pouziti)
- - Umět použít [cyklus for a while](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/cykly-jejich-syntaxe-a-pouziti)


## Analogový vstup
Digitální signál je nespojitý, má jen určité hodnoty (např. 0 a 1). Naproti tomu analogový signál je spojitý – může nabývat jakékoli hodnoty v čase. Příklad: zvukový signál v mikrofonu nebo napětí z teplotního čidla. 
![image](https://github.com/user-attachments/assets/2b732a50-2db1-4dce-9876-792f86aa4e0d)

Pro měření digitálního stavu pinu můžeme použít kterýkoli IO pin Arduina. Ovšem pro měření analogového signálu můžeme použít pouze piny označené písmenem A0-A7. Ty totiž lze připojit k AD převodníku na čipu mikroprocesoru (viz. [lekce ADC v MIT](https://tomaschovanec.github.io/MIT/13_ADC.html))

Pro samotné měření použijeme funkci analogRead(). Protože  A/D převodník v mikrokontroleru Arduina je 10-bitový, tzn. že rozeznává 2^10 (1024) hodnot napětí. Nulovému napětí odpovídá hodnota 0 a maximálnímu napětí (5V) hodnota 1023. Z toho vyplývá, že jeden "dílek" odpovídá: 5V/1024 tj. přibližně 4,88 mV. Pokud tedy naměříme např. hodnotu 724, tak napětí na vstupu je asi 3,53V.

## Měření napětí pomocí `analogRead()`
Pro měření napětí použijeme funkci `analogRead()`.  
Arduino má **10bitový A/D převodník**, což znamená, že dokáže rozlišit **2¹⁰ = 1024 úrovní napětí**.

- Hodnota **0** odpovídá **0 V**.  
- Hodnota **1023** odpovídá **5 V**.  
- Jeden „dílek“ tedy představuje:  
  \[
  5V / 1024 \approx 4,88 \text{ mV}
  \]

Například pokud `analogRead()` vrátí hodnotu **724**, vypočítáme napětí takto:  
\[
724 \times 4,88 \text{ mV} \approx 3,53 \text{ V}
\]  
**Napětí na vstupu je tedy přibližně 3,53 V.**


## Potenciometr
Potenciometr je nastavitelný rezistor, který umožňuje plynule měnit odpor v obvodu. Má tři vývody – dva krajní pro pevný odpor a střední (jezdec), kterým nastavujeme hodnotu odporu mezi jedním krajem a jezdcem. Tím, že měníme odpor, měníme i napětí v obvodu (dělič napětí).
![image](https://github.com/user-attachments/assets/64cce819-1b1f-4ab6-a5a2-6c1b35ec267e)

*Zdroj obrázku: https://www.electronicshub.org/how-potentiometer-works/*

- Umět k Arduinu připojit potenciometr a pomocí funkce [analogRead číst jeho polohu](https://bastlirna.hwkitchen.cz/arduino-zaklady-5-read-analog-voltage/)


## [Zpět na obsah](README.md)
