## Přidání knihovny do Arduina

Knihovny v Arduinu jsou předpřipravené balíčky kódu, které usnadňují práci s různými senzory, moduly nebo složitějšími funkcemi.
Proč používat knihovny? Zjednodušení kódu – nemusíš psát všechno od nuly, knihovna se postará o složitější části programu, např. komunikaci se senzorem.

### Přidání knihovny pomocí Library manageru

- V horním menu vyberte Tools > Manage Libraries…
- Do vyhledávacího pole napite název knihovny (nebo část názvu). Seznam knihoven se bude filtrovat podle toho, co píšte.
- Výsledky jsou seřazené abecedně, takže možná budete muset posunout dolů, než ji najdete.
- Nainstalujte knihovnu: Klikněte na zvolenou knihovnu. Můžete si přečíst popis a jméno autora. Pak klikněte na "Install". Arduino IDE automaticky vybere nejnovější verzi knihovny.
  
![image](https://github.com/user-attachments/assets/1dd94d18-4994-4dde-9b1e-e68cc9587888)


### Přidání knihovny ze zip souboru
- V horním menu vyberte: Sketch > Include Library > Add .ZIP Library…
- V dialogovém okně najděte soubor s knihovnou s příponou .zip a klikni na Open.
- Knihovna se automaticky rozbalí a přidá mezi ostatní knihovny. Najdete ji pak v Sketch  → Include library.

## Teplotní a vlhkostní čidlo DHT11
![image](https://github.com/user-attachments/assets/6f302fde-7002-46a4-9dac-08bd8cdb30da)


DHT11 je jednoduché digitální čidlo, které měří teplotu a vlhkost. Připojuje se k Arduinu 3 piny: VCC, GND, DATA. Má plastové pouzdro s otvory pro proudění vzduchu a uvnitř obsahuje:

- **Teplotní senzor** — měří teplotu v rozsahu 0–50 °C s přesností ±2 °C.
- **Senzor vlhkosti** — měří relativní vlhkost v rozsahu 20–90 % s přesností ±5 %.
- **Digitální komunikaci** — data posílá po jediném datovém pinu v digitálním formátu.

![image](https://github.com/user-attachments/assets/f7816d45-ff25-4df3-ad74-6a9cdfc20167)

![image](https://github.com/user-attachments/assets/7a04283b-2c96-4b60-8328-cd3b5d107ec3)

*Zdroj obrázků: https://howtomechatronics.com/tutorials/arduino/dht11-dht22-sensors-temperature-and-humidity-tutorial-using-arduino/ *

![image](https://github.com/user-attachments/assets/243bede4-bb75-435e-8b21-c4da6e532cab)

Příklad kódu s knihovnou [DHTlib by Rob Tillaart](https://github.com/RobTillaart/Arduino/tree/master/libraries/DHTlib):

```c
#include <dht.h>        // Include library

dht sensor;             // Creates a DHT object
int outPin = 2;        // Defines pin number to which the sensor is connected

void setup() {
	Serial.begin(9600);
}

void loop() {
	int readData = sensor.read11(outPin);	// Starts the conversion

	float temp = sensor.temperature;        // Read temperature
	float humid = sensor.humidity;           // Read humidity

	Serial.print("Temperature = ");
	Serial.print(temp);
	Serial.print("°C ");
	Serial.print("Humidity = ");
	Serial.print(humid);
	Serial.println("% ");
	Serial.println("");

	delay(2000); // wait two seconds
}
```

## LCD displej

<img src="https://github.com/user-attachments/assets/bca81828-3aa8-42fd-a01e-f5fd5cd19ad4" width="900"/>

![image](https://github.com/user-attachments/assets/b6db3a5d-ad19-4cc1-95c1-e09f09fd3db1)

![image](https://github.com/user-attachments/assets/78b70043-0437-481e-8bdc-5a0c43e8cd9d)

- Umět pracovat s [LCD displejem s I2C modulem](https://navody.dratek.cz/zaciname-s-arduinem/lcd-displej.html) knihovna k displeji [zde](https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library/archive/refs/heads/master.zip)

## I2C sběrnice
I2C (Inter-Integrated Circuit) je sériová sběrnice, která umožňuje komunikaci mezi více zařízeními (senzory, displeje, moduly) pomocí pouze dvou vodičů:
- SDA (Data) – přenáší data mezi zařízeními.
- SCL (Clock) – řídí časování přenosu dat.

Výhody I2C s Arduinem
- Úspora pinů – stačí jen 2 dráty pro připojení více zařízení (každé má unikátní adresu).
- Jednoduché zapojení – méně kabelů, méně zmatků.
- Podpora knihoven – Arduino má knihovny jako Wire.h pro snadné ovládání.
- Možnost rozšíření – připojení až 128 zařízení na stejnou sběrnici (adresy 7bit).
- Obousměrná komunikace – Master (Arduino) může posílat i přijímat data.
 
![image](https://github.com/user-attachments/assets/abc6c42b-abeb-4a6f-a850-ca47433e5dd9)
 
*Zdroj obrázku: https://www.hibit.dev/posts/102/communication-protocols-uart-i2c-and-spi*

### Práce s LCD displejem a knihovnou ???

```#include <LiquidCrystal_I2C.h>``` Načte knihovnu pro ovládání LCD displeje s I2C adaptérem.

```LiquidCrystal_I2C lcd(0x27, 16, 2);``` Vytvoří objekt lcd s adresou 0x27. 16, 2 znamená, že displej má 16 sloupců a 2 řádky.

```lcd.init();``` Inicializuje displej — připraví ho na použití.

```lcd.clear();```  Vyčistí obsah displeje.

```lcd.setCursor(0,1);``` Nastaví kurzor na 1. sloupec (indexuje se od 0) a 2. řádek.

```lcd.print("Hello world!");```  Vypíše text "Hello world!" od zadané pozice kurzoru.


## [Zpět na obsah](README.md)
