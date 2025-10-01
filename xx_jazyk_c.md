# Základy jazyka C

### Cíle lekce
- Vytvořit proměnnou, zapisovat do ní a číst z ní
- Používat pro opakovaný kód cyklus for nebo while

## Proměnné
Proměnná je pojmenované místo v paměti, kam můžeme uložit a kdykoliv změnit hodnotu.

Při pojmenovávání proměnných si dávejte pozor, aby jména měla smysl a popisovala, co proměnná obsahuje. Např. místo názvu ```x``` nebo ```a``` použijte něco jako ```teplota```, ```pocetHracu```, ```stavTlacitka``` – to pomůže, aby byl kód přehledný a snadno pochopitelný pro ostatní (i pro vás v budoucnu).

```c
// Příklad vytvoření a změny hodnoty proměnné
int cislo = 10;  // Proměnná "cislo" obsahuje hodnotu 10
cislo = 20;      // Změníme hodnotu na 20
cislo = cislo/2; // Vydělíme obsah proměnné 2
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
| `float`        | 32 bit  | Desetinné číslo (-3.4028235e38 až 3.4028235e38).        |
| `double`       | 64 bit  | Desetinné číslo s dvojnásobnou přesností.               |
| `string`       | různé   | Datový typ pro uchování textového řetězce.              |

## Podmínka, příkaz if-else

```c
int cislo=0;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    cislo++;
    if (cislo < 10) // Podmínka
    {
        Serial.println("Číslo je malé."); // Podmínka platí -> vypíše se text
    }
    else // Prvotní podmínka je neplatná
    {
        Serial.println("Číslo je velké."); // Podmínka neplatí -> vypíše se jiný text
    }
}
```

## Vícenásobná podmínka 
```c
int cislo=0;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    if (cislo > 0) {
        Serial.println("Číslo je kladné.");
    } else if (cislo < 0) {
        Serial.println("Číslo je záporné.");
    } else {
        Serial.println("Číslo je nula.");
    }
}
```


## Cyklus for
Pokud chceme nějakou část kódu opakovat můžeme použít for cyklus.
```c
for (inicializace; podmínka; aktualizace) {
    // kód, který se opakuje
}
```

Popis částí:
- Inicializace: Nastaví počáteční hodnotu proměnné (např. int i = 0)
- Podmínka: Kontroluje, jestli má cyklus pokračovat (např. i < 5)
- Aktualizace: Změní hodnotu proměnné po každé iteraci (např. i++)


Příklad for cyklu
```c
void setup() {
  Serial.begin(9600);  // Spustíme sériovou komunikaci

  // Kód v těle cyklu se provede 5x,  pro hodnoty i 0,1,2,3,4
  for (int i = 0; i < 5; i++) {
    Serial.print("Číslo: ");
    Serial.println(i);
  }
}

void loop() {
  // loop je prázdná, protože výpis se provede jen jednou při startu
}

```

## Cyklus while

Další typ cyklu je while. Zatímco for používáme, když víme kolikrát se má cyklus opakovat, while je lepší, když nevíme předem, kdy má cyklus skončit (čekání na vstup, tlačítko atd.).

```c
while (digitalRead(2) == HIGH) {
  // čekám, dokud tlačítko není stisknuté
}
```

## Úkoly
1. Pomocí cyklu vypište do sériového monitoru čísla od 0 do 15 včetně
2. Pomocí cyklu vypište do sériového monitoru čísla od 10 do -5
3. Pomocí cyklu vypište do sériového monitoru sudá čísla od 2 do 20 včetně
4. Napište program, který po startu čeká, dokud není stisknuto tlačítko, pak 25x blikne LEDkou


## [Zpět na obsah](README.md)
