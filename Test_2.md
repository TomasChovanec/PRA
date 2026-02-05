## Zadání

## Zadání
- Připojte k Arduinu RGB LEDku tak aby se dala ovládat její intenzita (použijte piny, které podporují PWM) a naprogramujte Arduino tak, aby se po startu programu společně na 1s rozsvítila modrá a červená barva a pak zase obě zhasnuly.
- Vytvořte vlatní funkci ```void blinkGreen()```. Ta po zavolání jednou blikne příslušnou barvou RGB LEDky (300ms ON, 300ms OFF). Hint: [Definice vlastní funkce](/lekce/Definice_funkce.md)
- Upravte funkci tak, aby se vstupním argumentem dal nastavit počet bliknutí (tj. např. blinkGreen(10) by bliknulo zelenou ledkou desetkrát. Hint: Použijte uvnitř funkce for cyklus a v jeho podmínce použijte argument funkce.
- Upravte funkci tak, aby kromě počtu bliknutí měla ješte další vstupní parametr, který by udával intenzitu svitu LEDky v %. Např. blinkGreen(10,75); by bliknulo zelenou LEDkou desetkrát a intenzita svícení by byla 75%. Hint: použijte uvnitř funkce namísto digitalWrite funkci analogWrite
