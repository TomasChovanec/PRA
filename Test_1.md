## Zadání
- Připojte k Arduinu I2C LCD displej k Arduinu a ověřte funkčnost výpisem krátké zprávy (např. „RGB START“).

- Připojte RGB LED. Vývody pro zelenou a červenou barvu připojte k Arduinu na piny, které podporuje funkci PWM (např. D3, D5, D6, D9, D10 nebo D11). Nezapomeňte zapojit rezistor pro omezení proudu.

- Pomocí for cyklu postupně měňte jas jedné barvy od 0 do 255 po krocích 5. Jakmile jedna barva dosáhne maxima, začněte stejným způsobem měnit další barvu (postupně R → G). Každý krok změny jasu trvá 50 ms pomocí delay(50).

- Na LCD displeji zobrazujte aktuální hodnotu PWM pro obě barvy, například: "R:255   G:125"
