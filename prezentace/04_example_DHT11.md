### Příklad použití knihovny [DHTlib](https://github.com/RobTillaart/DHTlib/archive/refs/heads/master.zip) s teplotním čidlem DHT11

```c
#include <dht.h>        // Include library

dht DHT;                // Creates a DHT object
int outPin = 2;        // Defines pin number to which the sensor is connected

void setup() {
	Serial.begin(9600);
}

void loop() {
	int readData = DHT.read11(outPin);	// Starts the conversion

	float temp = DHT.temperature;        // Read temperature
	float humid = DHT.humidity;           // Read humidity

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
