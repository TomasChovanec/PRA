# Internet of Things

Internet věcí je propojení běžných zařízení do sítě, kde spolu mohou komunikovat a sdílet data bez přímého zásahu člověka.
Zařízení (např. senzory, termostaty, osvětlení, kamery, meteostanice) posílají údaje přes Wi-Fi, Bluetooth nebo jiné protokoly do cloudu, kde se data ukládají, vyhodnocují nebo dál zpracovávají. Například:

- chytrý dům (ovládání světel, topení, žaluzií)
- měření teploty, vlhkosti, spotřeby energie
- sledování polohy nebo stavu zařízení
- průmyslové a zemědělské senzory

<img width="600" alt="image" src="https://github.com/user-attachments/assets/744c6894-e7f3-4fa4-b635-8f8818019169" />

## Google Firebase
Firebase je cloudová platforma od Googlu, která umožňuje jednoduše ukládat a číst data z aplikací nebo IoT zařízení přes internet.
Pro IoT se často používá Realtime Database – databáze, kde se data mění okamžitě a lze je číst i zapisovat přes jednoduché HTTP požadavky (GET, PUT).

Základní vlastnosti:
- Realtime Database – ukládání dat ve formátu JSON
- Autentizace uživatelů (není nutná v test režimu)
- Webová konzole pro sledování dat


Užitečné odkazy:
- [Oficiální web Firebase](https://firebase.google.com/)
- [Návod: Arduino + Firebase](https://randomnerdtutorials.com/esp32-firebase-realtime-database/)


## Deska Arduino Nano 33 IoT

Arduino Nano 33 IoT je moderní vývojová deska s vestavěným Wi-Fi modulem u-blox NINA-W102 a procesorem SAMD21 (ARM Cortex-M0+).
Oproti klasickému Arduinu UNO má tedy:
- jiný procesor (32bit ARM)
- integrované Wi-Fi a Bluetooth LE
- možnost přímé komunikace s webem nebo cloudem

Díky tomu se hodí pro IoT projekty, kde Arduino posílá data do internetu nebo přijímá příkazy z telefonu či webové aplikace.


<img width="595" height="403" alt="image" src="https://github.com/user-attachments/assets/85658303-de47-458b-9aca-aeb9ea23e033" />

Dále si přes Library manager nainstalujte knihovnu WifiNINA.

<img width="303" alt="image" src="https://github.com/user-attachments/assets/ba6db824-14e7-429e-aade-a5fb3c553457" />

## Pinout desky Arduino Nano 33 IoT
<img width="800" alt="image" src="https://github.com/user-attachments/assets/8b6e4e0b-ae7e-48f9-acf5-c86379dd0154" />


## Kostra programu pro čtení a zápis do Firebase
Kód demonstruje připojení Arduina k Wi-Fi, čtení a zápis hodnot do Firebase pomocí protokolu HTTPS a jednoduchého JSON formátu.

```c
#include <WiFiNINA.h>
#include <Arduino_JSON.h>
const char* ssid = "FrenGP.Cz-Vyuka";
const char* password = "heslo";
const char* host = "arduino-pokus-default-rtdb.firebaseio.com";
const int httpsPort = 443;
WiFiSSLClient client;
// --------------------------------------------------
// Připojení k Wi-Fi
void connect_to_wifi() {
  Serial.print("Připojuji se k WiFi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    WiFi.begin(ssid, password);
  }
  Serial.println("\nWiFi připojena!");
  Serial.print("IP adresa: ");
  Serial.println(WiFi.localIP());
}
// --------------------------------------------------
// Získání dat z Firebase (GET)
String get_data_from_firebase(String path) {
  if (client.connect(host, httpsPort)) {
    Serial.println("Připojeno k Firebase (GET)");
    String url = path + ".json";
    client.println("GET " + url + " HTTP/1.1");
    client.print("Host: "); client.println(host);
    client.println("Connection: close");
    client.println();
    // přeskočení hlaviček
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") break;
    }
    String payload = client.readString();
    client.stop();
    return payload;
  } else {
    Serial.println("Nepodařilo se připojit k Firebase (GET)!");
    return "";
  }
}
// --------------------------------------------------
// Odeslání dat do Firebase (PUT)
bool send_data_to_firebase(String path, String value) {
  if (client.connect(host, httpsPort)) {
    Serial.println("Připojeno k Firebase (PUT)");
    String url = path + ".json";
    client.println("PUT " + url + " HTTP/1.1");
    client.print("Host: "); client.println(host);
    client.println("Connection: close");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(value.length());
    client.println();
    client.println(value);
    // přeskočení hlaviček
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") break;
    }
    String response = client.readString();
    client.stop();
    Serial.print("Odpověď Firebase: ");
    Serial.println(response);
    return true;
  } else {
    Serial.println("Nepodařilo se připojit k Firebase (PUT)!");
    return false;
  }
}
// --------------------------------------------------
// Převedení JSON odpovědi na číslo
int parse_number(String payload) {
  JSONVar data = JSON.parse(payload);
  if (JSON.typeof(data) == "number") {
    return (int)data;
  } else {
    Serial.println("Chyba při čtení JSONu");
    return -999;
  }
}
// --------------------------------------------------
void setup() {
  Serial.begin(115200);
  while (!Serial);
  connect_to_wifi();
}
// --------------------------------------------------
void loop() {
  // 🔹 1. Zápis hodnoty do Firebase
  float teplota = 12.3;
  String value = String(teplota, 1); // druhý argument udává počet desetinných míst
  send_data_to_firebase("/Temperature_10", value);

  // 🔹 2. Čtení z Firebase
  String json = get_data_from_firebase("/Slider_10");
  int precteno = parse_number(json);
  Serial.print("Přečtená hodnota: ");
  Serial.println(precteno);
  delay(2000);
}

```

## Úkoly
1. Připojte potenciometr k Arduinu NANO 33 IoT, měřte a hodnotu odesílejte do Firebase pomocé funkce ```send_data_to_firebase("/Temperature_xxx", value);``` kde xxx bude číslo vaší Arduino sady. **Protože mikrokontroler použitý v Arduino Nano IoT neumožňuje 5V vstup, použijte pro napájení potenciometru 3,3V z pinu +3V3.**
2. Čtěte z Firebase hodnotu slideru pomocí funkce ```get_data_from_firebase("/Slider_xxx");``` (opět za xxx dosaďte číslo své sady) a nastavujte podle toho jas LEDky připojené k Arduinu (funkcí analogWrite)
3. Zkuste nastavovat stav LEDky z telefonu přes [https://tomaschovanec.github.io/PRA/iot](https://tomaschovanec.github.io/PRA/iot)

### [Zpět na obsah](../README.md)
