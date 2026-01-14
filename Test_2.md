## Zadání
- Připojte k Arduinu I2C LCD displej k Arduinu a ověřte funkčnost výpisem krátké zprávy (např. „RGB START“).

- Připojte k Arduinu RGB LEDku. Vývody pro zelenou a modrou barvu připojte k Arduinu na piny, které podporuje funkci PWM (např. D3, D5, D6, D9, D10 nebo D11). Nezapomeňte zapojit rezistor pro omezení proudu.

- Pomocí for cyklu postupně měňte jas jedné barvy od 0 do 250 po krocích 10. Každý krok změny jasu bude trvat 100ms.
   - nejprve cyklus pro zelenou (od 0 do 250, krok 10),
   - po jeho dokončení cyklus pro modrou (od 0 do 250, krok 10),

- Na LCD displeji zobrazujte aktuální hodnotu PWM pro obě barvy, například: "G:250   B:130"
