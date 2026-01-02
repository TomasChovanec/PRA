# Serial monitor, analogový vstup Arduina

### Cíle lekce
- Použít komunikaci přes sériový port k ověření funkce programu
- Zopakovat si základy jazyka C - práce s proměnnou, podmínka a cyklus
- Umět využívat funkci analogRead() pro měření napětí


<script type="text/javascript" id="MathJax-script" async 
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"> 
</script> 

## Sériová linka

`Serial.print()` se používá k odeslání dat do seriového monitoru. Můžete tak zobrazit hodnoty proměnných, zprávy nebo výsledky výpočtů během běhu programu.

- `Serial.print("text");` – vypíše text do seriového monitoru.  
- `Serial.print(variable);` – vypíše hodnotu proměnné.  
- `Serial.println()` Funguje stejně jako Serial.print() ale na konci přejde na nový řádek

### Příklad:
```cpp
int cislo = 5; // Proměnná, kterou poté budeme posílat

void setup()
{
Serial.begin(9600);
}

void loop()
{
Serial.print("Hodnota promenne cislo je: ");
Serial.println(cislo);  // Vytiskne "Hodnota x je: 10" a přejde na nový řádek
}
```

## Úkoly
1. Otevřete si program s blikáním LEDky a přidejte odesílání jednotlivých stavů (svítí/nesvítí) do serial monitoru.
1. Připojte k Arduinu tlačítko a napište program, který každých 500ms odesílá do sériového monitoru informaci o tom, zda je tlačítko stisknuto.
1. Napište program, který neustále inkrementuje (zvyšuje) hodnotu proměnné a posílá její hodnotu do sériového monitoru. Pomocí volby typu proměnné nebo velikosti inkrementu zajistěte, aby došlo k jejímu přetečení.
1. Pomocí cyklu vypište do sériového monitoru čísla od 0 do 15 včetně
1. Pomocí cyklu vypište do sériového monitoru čísla od 10 do -5
1. Pomocí cyklu vypište do sériového monitoru sudá čísla od 2 do 20 včetně
1. Napište program, který po startu čeká, dokud není stisknuto tlačítko, pak 25x blikne LEDkou


## Analogový vstup
Digitální signál je nespojitý, má jen určité hodnoty (např. 0 a 1). Naproti tomu analogový signál je spojitý – může nabývat jakékoli hodnoty v čase. Příklad: zvukový signál v mikrofonu nebo napětí z teplotního čidla. 
![image](../img/02_Zaklady_C_potenciometr_1.png)

Pro měření digitálního stavu pinu můžeme použít kterýkoli IO pin Arduina. Ovšem pro měření analogového signálu můžeme použít pouze piny označené písmenem A0-A7. Ty totiž lze připojit k AD převodníku na čipu mikroprocesoru (viz. [lekce ADC v MIT](https://tomaschovanec.github.io/MIT/13_ADC.html))

## Funkce analogRead()

Pro měření napětí použijeme funkci `analogRead()`. Jako argument funkci zadáme číslo pinu, na kterém chceme měřit. 
Tedy např. ```int napeti = analogRead(A4);```

Arduino má **10bitový A/D převodník**, což znamená, že dokáže rozlišit **$$2^{10} = 1024$$** úrovní napětí.

- Hodnota **0** odpovídá **0 V**.  
- Hodnota **1023** odpovídá **5 V**.  
- Jeden „dílek“ tedy představuje:  

$$  
\Large \frac{5V}{1024} = 4,88 \text{ mV}  
$$  

Například pokud `analogRead()` vrátí hodnotu **724**, vypočítáme napětí takto:  

$$  
\Large724 \times 4,88 \text{ mV} = 3,53 \text{ V}  
$$  

Napětí na vstupu je tedy přibližně 3,53 V.

## Potenciometr
Potenciometr je nastavitelný rezistor, který umožňuje plynule měnit odpor v obvodu. Má tři vývody – dva krajní pro pevný odpor a střední (jezdec), kterým nastavujeme hodnotu odporu mezi jedním krajem a jezdcem. Tím, že měníme odpor, měníme i napětí v obvodu (dělič napětí).

![image](../img/02_Zaklady_C_potenciometr_2.png)

*Zdroj obrázku: https://www.electronicshub.org/how-potentiometer-works/*

## Úkoly
1. Zapojte k Arduinu potenciometr, čtete hodnotu funkcí analogRead do proměnné a posílejte na sériovou linku
2. Hodnotu převeďte na napětí ve voltech a pošlete na sériovou linku
3. Pokud je vyšší než 2,5V, rozsviťte LEDku
4. Potenciometrem měňte frekvenci blikání LEDky

## [Zpět na obsah](README.md)
