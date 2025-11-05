# Test - displej, analogWrite()

1. Připojte I2C displej k Arduinu.
    - Použijte vhodnou knihovnu (např. LiquidCrystal_I2C) a ověřte funkčnost výpisem testovacího textu.
  
2. Připojte červenou LED k Arduinu.
    - Použijte pin, který podporuje funkci analogWrite()
  
3. Naprogramujte plynulou změnu jasu LED pomocí funkce analogWrite().
    - Jas zvyšujte od 0 do 250 po krocích 25.
    - Poté snižujte zpět z 250 na 0 opět po krocích 25.
    - Každý krok trvá 200 ms.
  
4. Zobrazujte aktuální hodnotu PWM signálu na displeji.
    - Například ve formátu: PWM = 120
