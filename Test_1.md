## Zadání
- Připojte k Arduinu I2C LCD displej a ověřte funkčnost výpisem krátké zprávy (např. „RGB START“).

- Připojte k Arduinu RGB LEDku. Vývody pro červenou a modrou barvu připojte k Arduinu na piny, které podporuje funkci PWM (např. D3, D5, D6, D9, D10 nebo D11). Nezapomeňte zapojit rezistor pro omezení proudu.

- Pomocí for cyklu postupně měňte jas jedné barvy od 0 do 240 po krocích 20. Každý krok změny jasu bude trvat 200ms.
   - nejprve cyklus pro červenou (od 0 do 240, krok 20),
   - po jeho dokončení cyklus pro modrou (od 0 do 240, krok 20),

- Na LCD displeji zobrazujte aktuální hodnotu PWM pro obě barvy, například: "Red:250   Blue:130"
