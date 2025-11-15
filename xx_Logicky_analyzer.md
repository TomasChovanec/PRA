# Logický analyzer

## Cíle lekce
- Porozumět základnímu principu logického analyzátoru.
- Naučit se zachytit a analyzovat PWM signál.
- Umět dekódovat UART komunikaci.
- Umět dekódovat I2C komunikaci.

## Co je logický analyzátor

<img width="1113" height="523" alt="image" src="https://github.com/user-attachments/assets/3a340a0b-d616-441f-9e0c-c7794c35d54c" />

Logický analyzátor je nástroj pro zachytávání digitálních signálů. Umožňuje:
	• připojit více kanálů současně (zde 8 kanálů),
	• zaznamenat jejich průběh v čase,
	• zobrazit změny stavu (LOW/HIGH),
	• automaticky dekódovat protokoly (UART, I2C, SPI atd.).
Typický analyzátor pracuje s napěťovou úrovní 0–5 V (ověřte specifikace!).

### Měření PWM signálu (např. Arduino analogWrite)
- Změřte periodu a frekvenci PWM signálu.
- CH0 → PWM pin Arduina.
- Střída (duty cycle) pro různé hodnoty analogWrite().

### Analýza UART komunikace
- CH1 → TX pin Arduina.
- Přidat protokol Async Serial.
- Nastavit parametry: přenosová rychlost (např. 9600), 8N1.
- Zachytit odesílaný text (např. "Ahoj").
- Vidět jednotlivé bity.
- Změřit, spočítat baudrate
	
### Měření I2C komunikace
Zapojení
- CH2 → SDA.
- CH3 → SCL.
- Přidat protokol I2C.


