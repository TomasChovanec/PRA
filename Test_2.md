## Zadání
- Připojte k Arduinu I2C LCD displej k Arduinu a ověřte funkčnost výpisem krátké zprávy (např. „RGB START“).

- Připojte RGB LED. Vývody pro zelenou a modrou barvu připojte k Arduinu na piny, které podporuje funkci PWM (např. D3, D5, D6, D9, D10 nebo D11).

- Pomocí for cyklu postupně měňte jas jedné barvy od 0 do 250 po krocích 10. Jakmile jedna barva dosáhne maxima, začněte stejným způsobem měnit další barvu (postupně G → B). Každý krok změny jasu trvá 100 ms pomocí delay(100).

- Na LCD displeji zobrazujte aktuální hodnotu PWM pro obě barvy, například: "B:255   B:125"
