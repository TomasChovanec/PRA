### Teplotní čidlo, LCD displej

Po této lekci byste měli: 

- Umět do Arduino IDE nainstalovat knihovnu

## Teplotní a vlhkostní čidlo DHT-11

DHT11 je jednoduché digitální čidlo, které měří teplotu a vlhkost. Má plastové pouzdro s otvory pro proudění vzduchu a uvnitř obsahuje:

![image](https://github.com/user-attachments/assets/243bede4-bb75-435e-8b21-c4da6e532cab)

Teplotní senzor — měří teplotu v rozsahu 0–50 °C s přesností ±2 °C.

Senzor vlhkosti — měří relativní vlhkost v rozsahu 20–90 % s přesností ±5 %.

Jednožilovou komunikaci — data posílá po jediném datovém pinu v digitálním formátu.

Čidlo je levné, snadno se připojuje k Arduinu (3 piny: VCC, GND, DATA) a funguje s knihovnami jako DHT.h. Hodí se pro jednoduché projekty s měřením podmínek v místnosti.


```c
#include <dht.h>        // Include library

dht sensor;                // Creates a DHT object
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

## LCD display

<img src="https://github.com/user-attachments/assets/bca81828-3aa8-42fd-a01e-f5fd5cd19ad4" width="900"/>

![image](https://github.com/user-attachments/assets/b6db3a5d-ad19-4cc1-95c1-e09f09fd3db1)

- Umět pracovat s [LCD displejem s I2C modulem](https://navody.dratek.cz/zaciname-s-arduinem/lcd-displej.html) knihovna k displeji [zde](https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library/archive/refs/heads/master.zip)

## I2C sběrnice
- Chápat co je to [I2C sběrnice](https://cs.wikipedia.org/wiki/I%C2%B2C) a k čemu slouží
- 
    ![image](https://github.com/user-attachments/assets/abc6c42b-abeb-4a6f-a850-ca47433e5dd9)
 
  *Zdroj obrázku: https://www.hibit.dev/posts/102/communication-protocols-uart-i2c-and-spi*


## [Zpět na obsah](README.md)
