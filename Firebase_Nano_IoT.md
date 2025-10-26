# Internet of things

- Stručně princip, příklady použití

## Google Firebase
- Co to je, odkaz na tutorialy

<img width="1080" height="756" alt="image" src="https://github.com/user-attachments/assets/744c6894-e7f3-4fa4-b635-8f8818019169" />

## Deska Arduino Nano 33 IoT

Jiný procesor, wifi

<img width="318" height="207" alt="image" src="https://github.com/user-attachments/assets/70114d5e-8089-4350-8b2f-e53840de0520" />

<img width="303" height="177" alt="image" src="https://github.com/user-attachments/assets/752209db-3e17-471b-872d-e170f6e80c9d" />


<img width="862" height="851" alt="image" src="https://github.com/user-attachments/assets/8b6e4e0b-ae7e-48f9-acf5-c86379dd0154" />


## Kostra programu pro čtení a zápis do Firebase

```c
#include <WiFiNINA.h>
#include <Arduino_JSON.h>
const char* ssid = "mojeWiFi";
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
  float teplota = random(200, 300) / 10.0;  // simulace 20.0–30.0
  String value = String(teplota, 1);
  send_data_to_firebase("/Temperature_1", value);
  // 🔹 2. Čtení z Firebase
  String json = get_data_from_firebase("/Temperature_2");
  int precteno = parse_number(json);
  Serial.print("Přečtená teplota: ");
  Serial.print(precteno);
  Serial.println(" °C");
  delay(2000);
}

```

## Úkoly
1. Připojte potenciometr, měřte a hodnotu odesílejte do Firebase
2. čtěte z Firebase a nastavujte podle toho LEDku
3. Zkuste natsavovat LEDku z telefonu

### [Zpět na obsah](README.md)
