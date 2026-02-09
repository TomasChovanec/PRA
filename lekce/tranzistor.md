# Spínání větších proudů pomocí tranzistoru

V dnešní lekci budeme Arduinem řídit malý ventilátor. Ventilátor je vyroben pro napájecí napětí 5V. Nejsnazší by bylo připojit ventilátor přímo na nějaký digitální pin Arduina a zapínat ho funkcí ```digitalWrite()```. Musíme ale ověřit, zda není proudový odběr ventilátoru příliš velký, což by mohlo způsobit zničení Arduina.

<img width="382" height="282" alt="image" src="https://github.com/user-attachments/assets/cc13d7e0-9231-48eb-8649-f51b7cced807" />


## Jaký proud můžeme odebírat z pinu Arduina?
Pokud se podíváme do datasheetu mikrokontroleru ATmega328, který je použit v desce Arduino UNO, se kterou na cvičení pracujeme, najdeme tam v sekci Absolute maximum ratings toto:

<img width="902" height="383" alt="image" src="https://github.com/user-attachments/assets/ed31257e-5361-461e-8d1f-1b83f337eea9" />

## Jaký proud odebírá ventilátor?
Pokud nevíme, jaký proud ventilátor odebírá, můžeme ho snadno změřit.

**Úkol 1:**
Nakreslete schéma ventilátoru spínaného tlačítkem (Arduino použijte jen jako zdroj napětí 5V). Do schematu zakreslete i ampermetr, kterým změříte proudový odběr ventilátoru. Jako schematickou značku pro ventilátor můžete použít např. značku motoru.

<img width="173" height="52" alt="image" src="https://github.com/user-attachments/assets/e12c4737-9c63-4514-9941-c9909a8628b2" />


**Úkol 2:**
Vezměte si multimetr, vysvětlete, jak postupovat při měření proudu a jaká jsou rizika? Jak postupovat při volbě rozsahu?
<img width="351" height="471" alt="image" src="https://github.com/user-attachments/assets/8c84a646-b4bc-4332-9b58-54cce8dcd72a" />

**Úkol 3:**
Změřte proud ventilátoru a porovnejte ho s maximálním proudem z pinu Arduina.



