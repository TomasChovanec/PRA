## Fotorezistor

![image](https://github.com/user-attachments/assets/8741bca8-a22a-43d7-b47f-33488a30549a)

Fotorezistor je polovodičová součástka, která mění svůj odpor v závislosti na osvětlení - čím více fotonů na něj dopadá, tím více se v něm tvoří volných elektronů a roste jeho vodivost. Fotorezistor, který budeme používat na cvičení má odpor při 10 Luxech 10-20kΩ, odpor v temnu: 1MΩ.

Pokud jej zapojíme spolu s pevným rezistorem jako dělič napětí, můžeme pak AD převodníkem měřit spojitě intenzitu světla.

### Zadání:

**1.** Zapojte k Arduinu napěťový dělič s fotorezistorem a na serial monitoru zobrazujte intenzitu osvětlení

**2.** Pomocí LEDky na Arduino desce indukujte, zda je v místnosti světlo nebo tma. Hraniční hodnotu si určete dle svého uvážení.

**3.** Připojte k Arduinu servo a simulujte zavírání žaluzií na základě slunečního svitu 
- při dostatečném osvětlení (nad nastavenou hranicí) se žaluzie plynule zavřou (servo se přesune na 90°).
- při slabém osvětlení (pod hranicí) se žaluzie plynule otevřou (0°).
      
**4.** Zajistěte, aby se žaluzie neustále nehýbaly při kolísání intenzity světla kolem hraniční hodnoty. Implementujte hysterezi – nastavte různé prahy pro zavření a otevření žaluzií, aby servo nereagovalo na malé změny světla.


<img src="https://github.com/user-attachments/assets/7c966978-5c7d-47f2-86e8-cbc1e7beea6e" width="600"/>

*Zdroj obrázku: https://www.lorric.com/en/Articles/flowmeter-technology/flowmeter-technology/hysteresis-function*

**5.** Zabraňte tomu, aby žaluzie reagovaly okamžitě na každé krátké zastínění senzoru (např. když kolem projde člověk). Stav žaluzií se změní pouze tehdy, pokud světlo nebo tma trvá déle než 5 sekund.

