# Test - displej, analogWrite()

1. Připojte I2C displej k Arduinu.
    - Použijte vhodnou knihovnu (např. LiquidCrystal_I2C) a ověřte funkčnost výpisem testovacího textu.
  
2. Připojte červenou LED k Arduinu.
    - Použijte pin, který podporuje funkci analogWrite()
    - Nezapomeňte zapojit rezistor pro omezení proudu.
  
3. Naprogramujte plynulou změnu jasu LED pomocí funkce analogWrite().
    - Jas zvyšujte od 0 do 255 po krocích 10.
    - Poté snižujte zpět na 0 opět po krocích 10.
    - Každý krok trvá 100 ms.
  
4. Zobrazujte aktuální hodnotu PWM signálu na displeji.
    - Například ve formátu: PWM = 120
