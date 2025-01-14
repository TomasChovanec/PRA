# Funkce millis()

- počet milisekud od startu programu
- Poznámka: K přetečení časovače dojde přibližně jednou za 50 dní. (4 294 967 295 ms = 4 294 967 s = 71 582 min = 1193 h = 49,7 dní)
- datový typ unsigned long
- serial.println(millis) ->reset
- blikat jednou ledkou s millis


## Multitasking
Když jsme doteď chtěli nastavit v programu nějaké časování (např blikat LEDkou jednou za sekundu), používali jsme funkci delay(). Výhoda této funkce je, že je jednoduchá a snadno se používá. Ale nevýhodou je, že během čekání ve funkci dleay() nemůže procesor dělat nic jiného. Pokud děláme jednoduchý program, který dělá jen jednu věc, tak nám to nevadí.

Např. pokud chceme blikat jednou LEDkou s frekvencí 1Hz (jednou za sekundu), není to problém:

```C
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
```

Co ale když budeme k příkladu výše chtít přidat druhou LEDku a tou blikat 10x za sekundu? 


[Video k funkci millis()](https://www.youtube.com/watch?v=BYKQ9rk0FEQ&ab_channel=ProgrammingElectronicsAcademy)

[Tutorial k millis()](https://bastlirna.hwkitchen.cz/arduino-zaklady-blikani-bez-funkce-delay/)
