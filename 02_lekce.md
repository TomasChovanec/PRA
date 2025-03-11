<script type="text/javascript" id="MathJax-script" async 
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"> 
</script> 


## Proměnné
Proměnná je pojmenované místo v paměti, kam můžeme uložit a kdykoliv změnit hodnotu.

Proměnná nesmí mít v názvu diakritiku ani mezeru.

Při pojmenovávání proměnných si dávejte pozor, aby jména měla smysl a popisovala, co proměnná obsahuje. Např. místo názvu ```x``` nebo ```a``` použijte něco jako ```teplota```, ```pocetHracu```, ```stavTlacitka``` – to pomůže, aby byl kód přehledný a snadno pochopitelný pro ostatní (i pro vás v budoucnu).

```c
// Příklad vytvoření a změny hodnoty proměnné
int cislo = 10;  // Proměnná "cislo" obsahuje hodnotu 10
cislo = 20;      // Změníme hodnotu na 20
cislo = cislo/2;      // Vydělíme obsah proměnné 2
```

V jazyce C musíme při vytvoření proměnné zadat i její datový typ. Ten vybereme podle toho, jaká data chceme do proměnné ukládat.

| Datový typ       | Velikost | Popis |
|------------------|---------|-----------------------------------------------------------|
| `char`          | 8 bit   | Znak, nabývá hodnoty jednoho ASCII znaku (-128 až 127).  |
| `byte`          | 8 bit   | Ukládá 8bitové číslo v rozsahu (0 až 255).               |
| `boolean`       | 8 bit   | Logická hodnota `true` (1) / `false` (0).               |
| `int`           | 16 bit  | Celé číslo (-32 768 až 32 767).                         |
| `unsigned int`  | 16 bit  | Pouze kladná čísla (0 až 65 535).                       |
| `long`         | 32 bit  | Celé číslo (-2 147 483 648 až 2 147 483 647).           |
| `unsigned long` | 32 bit  | Pouze kladná čísla (0 až 4 294 967 295).                |
| `float`        | 32 bit  | Desetinné číslo (-3.4028235E38 až 3.4028235E38).        |
| `double`       | 64 bit  | Desetinné číslo s dvojnásobnou přesností.               |
| `string`       | různé   | Datový typ pro uchování textového řetězce.              |


## Sériová linka
- Umět posílat data do PC pomocí fuknce Serial.print

## Podmínky, cykly
- Umět použít [podmínku if-else](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/podminky-a-jejich-pouziti)
- Umět použít [cyklus for a while](https://www.itnetwork.cz/hardware-pc/arduino/programovaci-jazyk/cykly-jejich-syntaxe-a-pouziti)

## Analogový vstup
Digitální signál je nespojitý, má jen určité hodnoty (např. 0 a 1). Naproti tomu analogový signál je spojitý – může nabývat jakékoli hodnoty v čase. Příklad: zvukový signál v mikrofonu nebo napětí z teplotního čidla. 
![image](https://github.com/user-attachments/assets/2b732a50-2db1-4dce-9876-792f86aa4e0d)

Pro měření digitálního stavu pinu můžeme použít kterýkoli IO pin Arduina. Ovšem pro měření analogového signálu můžeme použít pouze piny označené písmenem A0-A7. Ty totiž lze připojit k AD převodníku na čipu mikroprocesoru (viz. [lekce ADC v MIT](https://tomaschovanec.github.io/MIT/13_ADC.html))

Pro samotné měření použijeme funkci analogRead(). Protože  A/D převodník v mikrokontroleru Arduina je 10-bitový, tzn. že rozeznává 2^10 (1024) hodnot napětí. Nulovému napětí odpovídá hodnota 0 a maximálnímu napětí (5V) hodnota 1023. Z toho vyplývá, že jeden "dílek" odpovídá: 5V/1024 tj. přibližně 4,88 mV. Pokud tedy naměříme např. hodnotu 724, tak napětí na vstupu je asi 3,53V.

## Měření napětí s Arduinem

Pro měření napětí použijeme funkci `analogRead()`. Jako argument funkci zadáme číslo pinu, na kterém chceme měřit. 
Tedy např. ```int napeti = analogRead(A4);```

Arduino má **10bitový A/D převodník**, což znamená, že dokáže rozlišit **$2^{10} = 1024$** úrovní napětí.

- Hodnota **0** odpovídá **0 V**.  
- Hodnota **1023** odpovídá **5 V**.  
- Jeden „dílek“ tedy představuje:  

$$  
\Large \frac{5V}{1024} = 4,88 \text{ mV}  
$$  

Například pokud `analogRead()` vrátí hodnotu **724**, vypočítáme napětí takto:  

$$  
\Large724 \times 4.88 \text{ mV} = 3,53 \text{ V}  
$$  

Napětí na vstupu je tedy přibližně 3,53 V.

## Potenciometr
Potenciometr je nastavitelný rezistor, který umožňuje plynule měnit odpor v obvodu. Má tři vývody – dva krajní pro pevný odpor a střední (jezdec), kterým nastavujeme hodnotu odporu mezi jedním krajem a jezdcem. Tím, že měníme odpor, měníme i napětí v obvodu (dělič napětí).
![image](https://github.com/user-attachments/assets/64cce819-1b1f-4ab6-a5a2-6c1b35ec267e)

*Zdroj obrázku: https://www.electronicshub.org/how-potentiometer-works/*


## [Zpět na obsah](README.md)
