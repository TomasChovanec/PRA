# Logický analyzer

## Cíle lekce
- Porozumět základnímu principu logického analyzátoru.
- Naučit se zachytit a analyzovat PWM signál.
- Umět dekódovat UART komunikaci.
- Umět dekódovat I2C komunikaci.

## Co je logický analyzátor

<img width="1113" height="523" alt="image" src="https://github.com/user-attachments/assets/3a340a0b-d616-441f-9e0c-c7794c35d54c" />

Logický analyzátor je nástroj pro zachytávání digitálních signálů. 
Umožňuje:
- měřit více kanálů současně (zde 8 kanálů),
- zaznamenat jejich průběh v čase,
- zobrazit změny stavu (LOW/HIGH),
- měřit časové intervaly
- automaticky dekódovat protokoly (UART, I2C, SPI atd.).

Typický analyzátor pracuje s napěťovou úrovní 0–5 V (ověřte specifikace!).

### Měření PWM signálu (např. Arduino analogWrite)
- Připojte k Arduinu potenciometr a podle jeho polohy nastavujte PWM na LEDce na pinu 13.
- Připojte logický analyzer na pin 13
- Změřte periodu a frekvenci PWM signálu.
- Sledujte střídu (duty cycle) pro různé hodnoty analogWrite().

### Analýza UART komunikace
- Rozšiřte program z předchozího bodu tak, aby jednou za 100ms odeslal na sériový port informaci o aktuálním stavu PWM (Např. "PWM je 255")
- Připojte logický analyzer CH1 → TX pin Arduina.
- Přidejte protokol Async Serial a nastavte přenosovou rychlost (např. 9600)
- Zkuste přečíst odesílaný text a sledujte jak je zakódován
- Změřte délku jednoho bitu a spočítejte baudrate
	
### Měření I2C komunikace
- Rozšiřte program z předchozího bodu tak, že informaci o aktuálním stavu PWM zobrazíte i na LCD displeji
- Připojte logický analyzer - CH2 → SDA, CH3 → SCL.
- Přidejte protokol I2C.
- Sledujte dekódovanou komunikaci, zkuste vysvětlit, jak funguje hodinový signál


