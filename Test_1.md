# Test - cykly, analogRead(), analogWrite()

1. Do nepájivého pole zapojte LED diodu s rezistorem (cca 220 Ω) a připojte ji na nějaký pin Arduina, který podporuje PWM výstup.
2. Naprogramujte arduino tak, aby po každém resetu touto LEDkou 7x bliknulo (300ms ON/30ms OFF)
3. Připojte potenciometr jako napěťový dělič, střední vývod na analogový vstup A0
4. Pomocí funkce analogRead() získejte hodnotu děliče (0–1023) a vypište ji na sériový monitor.
5. Převádějte hodnotu potenciometru na rozsah 0–255 (např. pomocí funkce map) a použijte funkci analogWrite() k nastavení jasu LED.
