# Samostatná práce ve dvojicích

## Automatický ovladač střešního okna
Vaším úkolem je vytvořit zapojení a naprogramovat ovladač střešního okna s automatickým návratem do výchozí polohy.

### Požadavky na funkčnost:
**Ovládání pohybu:**
- Otevření okna bude prováděno buď servem, nebo krokovým motorem (volba je na vás).
- Úhel otevření se bude zadávat přes sériovou linku v rozsahu 0–180°.

**Zpracování vstupu:**
- Pokud je zadaný úhel mimo rozsah 0–180°, program musí odeslat chybovou hlášku do sériového monitoru a úhel ignorovat.
- Pokud je vstup platný, okno se okamžitě nastaví do požadovaného úhlu.

**Automatický návrat:**
- Po 10 sekundách od poslední změny se okno automaticky zavře (vrátí na 0°).
- Pokud během této doby přijde nový platný úhel, musí se okno okamžitě přesunout do nové polohy a časovač návratu se restartuje.
