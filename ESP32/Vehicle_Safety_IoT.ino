#include <WiFi.h>
#include <PubSubClient.h>

char ssid[] = "Sid";
char pass[] = "06092803";

// Ubuntu MQTT Broker IP
const char* mqtt_server = "192.168.6.253";
WiFiClient espClient;
PubSubClient client(espClient);

// UART Data
String uartData = "";
char packet[60];

int distance = 0;
int temperature = 0;
int gas = 0;
int rain = 0;

void reconnect()
{
  while (!client.connected())
  {
    Serial.print("Connecting to MQTT... ");

    if (client.connect("ESP32_Vehicle"))
    {
      Serial.println("Connected");
    }
    else
    {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying...");
      delay(3000);
    }
  }
}

void setup()
{
  Serial.begin(115200);

  Serial2.begin(115200, SERIAL_8N1, 16, 17);

  WiFi.begin(ssid, pass);

  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected");

  client.setServer(mqtt_server, 1883);
}

void loop()
{
  if (!client.connected())
  {
    reconnect();
  }

  client.loop();

  while (Serial2.available())
  {
    char c = Serial2.read();

    Serial.print(c);

    if (c == '\n')
    {
      uartData.trim();

      if (uartData.startsWith("CAN,"))
      {
        uartData.toCharArray(packet, sizeof(packet));

        if (sscanf(packet,
                   "CAN,%d,%d,%d,%d",
                   &distance,
                   &temperature,
                   &gas,
                   &rain) == 4)
        {
          char payload[150];

          sprintf(payload,
                  "{\"distance\":%d,\"temperature\":%d,\"gas\":%d,\"rain\":%d}",
                  distance,
                  temperature,
                  gas,
                  rain);

          Serial.println(payload);

          client.publish("vehicle/safety", payload);
        }
      }

      uartData = "";
    }
    else
    {
      uartData += c;
    }
  }
}