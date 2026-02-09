# Ovládání ventilátoru Arduinem

V dnešní lekci budeme Arduinem řídit malý ventilátor. Ventilátor, který máme k dispozici je vyroben pro napájecí napětí 5V. Nejsnazší by bylo připojit ventilátor přímo na nějaký digitální pin Arduina a zapínat ho funkcí ```digitalWrite()```. Musíme ale ověřit, zda není proudový odběr ventilátoru příliš velký, což by mohlo způsobit zničení Arduina.

<img width="382" height="282" alt="image" src="https://github.com/user-attachments/assets/cc13d7e0-9231-48eb-8649-f51b7cced807" />


## Jaký proud můžeme odebírat z pinu Arduina?
Pokud se podíváme do datasheetu mikrokontroleru ATmega328, který je použit v desce Arduino UNO, se kterou na cvičení pracujeme, najdeme tam v sekci Absolute maximum ratings toto:

<img width="902" height="383" alt="image" src="https://github.com/user-attachments/assets/ed31257e-5361-461e-8d1f-1b83f337eea9" />

## Jaký proud odebírá ventilátor?
Pokud nevíme (např. z dokumentace), jaký proud ventilátor odebírá, můžeme ho snadno změřit.

**Úkol 1:**
Nakreslete schéma ventilátoru spínaného tlačítkem (Arduino použijte jen jako zdroj napětí 5V). Do schématu zakreslete i ampermetr, kterým změříte proudový odběr ventilátoru. Jako schematickou značku pro ventilátor můžete použít např. značku motoru.

<img width="173" height="52" alt="image" src="https://github.com/user-attachments/assets/e12c4737-9c63-4514-9941-c9909a8628b2" />


**Úkol 2:**
Vezměte si multimetr, vysvětlete, jak postupovat při měření proudu a jaká jsou rizika? Jak postupovat při volbě rozsahu?
<img width="351" height="471" alt="image" src="https://github.com/user-attachments/assets/8c84a646-b4bc-4332-9b58-54cce8dcd72a" />

**Úkol 3:**
Změřte proud ventilátoru a porovnejte ho s maximálním proudem z pinu Arduina. Můžeme ventilátor napájet přímo z digitálního pinu Arduina?

## Použití tranzistoru jako výkonového spínače

**Úkol 4:**
Pin Arduina nám tedy na napájení ventilátoru nestačí. Můžeme pro spínání použít NPN tranzistor BC337, který máme k dispozici. Popište, jak funguje zapojení tranzistoru se společným emitorem a jak ho můžeme použít pro spínání ventilátoru.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/748a58ee-fcab-47d5-abd8-f9bc8b0ab6a0" />

<img width="500" alt="image" src="https://github.com/user-attachments/assets/4bc8a3a3-979a-41a1-9fa4-98c0e4a981c9" />

**Úkol 5:**
Nakreslete schéma obvodu se společným emitorem. Pro ovládání bázového proudu použijte tlačítko. Jako bázový rezistor použijte 220R.

**Úkol 6:**
Podle schématu z bodu 5 proveďte zapojení na nepájivém poli. Z [datasheetu tranzistoru BC337](https://www.farnell.com/datasheets/1789499.pdf) zjistěte pinout (který pin je kolektor atd) a ověřte, že tranzistor dokáže spínat proud pro ventilátor.

**Úkol 7:**
Namísto ovládacího tlačítka použijte pro řízení báze tranzistoru digitální pin Arduina. Dále připojte k Arduinu teplotní senzor a naprogramujte Arduino tak, aby se ventilátor spínal při teplotách >25°C.

