# Od Arduino funkcí k registrům

```c
int main(void)
{
    init();          // inicializace hardware (timery, UART...)
    setup();         // uživatelský setup

    while (1)
    {
        loop();      // uživatelská smyčka
    }
}
```

## Přiřazení pinů Arduina k portům mikrokontroleru
<img width="700" alt="image" src="https://github.com/user-attachments/assets/10424de5-d163-49e9-b062-c5cca09aba09" />


## Úkoly

1. Zablikat LEDKou bez použití pinMode() a digitalWrite(). Delay() použít můžete. Viz [lekce MIT](https://tomaschovanec.github.io/MIT/02_Blikani_LED.html)

2. Blikat LEDkou s periodou 100ms bez použití funkce delay, pouze pomocí časovače Timer1 viz [lekce MIT](https://tomaschovanec.github.io/MIT/08_Timer.html)

