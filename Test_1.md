## Zadání
- Připojte k Arduinu RGB LEDku tak aby se dala ovládat její intenzita (použijte piny, které podporují PWM) a naprogramujte Arduino tak, aby se po startu programu společně na 1s rozsvítila modrá a červená barva
- Vytvořte vlatní funkci ```void blinkRed()```. Ta po zavolání jednou blikne příslušnou barvou RGB LEDky (500ms ON, 500ms OFF). Hint: [Definice vlastní funkce](/lekce/Definice_funkce.html)
- Upravte funkci tak, aby se vstupním argumentem dal nastavit počet bliknutí (tj. např. blinkRed(10) by bliknulo červenou ledkou desetkrát. Hint: Použijte uvnitř funkce for cyklus a v jeho podmínce použijte argument funkce.
- Upravte funkci tak, aby kromě počtu bliknutí měla ješte další vstupní parametr, který by udával intenzitu svitu LEDky v %. Např. blinkRed(10,75); by bliknulo červenou LEDkou desetkrát a intenzita svícení by byla 75%. Hint: použijte uvnitř funkce namísto digitalWrite funkci analogWrite
