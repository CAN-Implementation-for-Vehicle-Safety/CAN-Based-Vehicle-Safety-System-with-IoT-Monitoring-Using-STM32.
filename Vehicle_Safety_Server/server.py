from flask import Flask
import json
import paho.mqtt.client as mqtt

from config import *
from database import insert_data

app = Flask(__name__)

# -------------------- MQTT CALLBACKS --------------------

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to MQTT Broker")

    client.subscribe(MQTT_TOPIC)

    print(f"Subscribed to : {MQTT_TOPIC}")


def on_message(client, userdata, msg):

    try:

        payload = msg.payload.decode()

        print("\nReceived :", payload)

        data = json.loads(payload)

        distance = data["distance"]
        temperature = data["temperature"]
        gas = data["gas"]
        rain = data["rain"]

        insert_data(distance, temperature, gas, rain)

    except Exception as e:

        print("Error :", e)


# -------------------- MQTT CLIENT --------------------

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)

client.loop_start()

# -------------------- FLASK --------------------

@app.route('/')

def home():

    return "Vehicle Safety MQTT Server Running"


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)