from flask import Flask, render_template
import json
import paho.mqtt.client as mqtt

from config import *
from database import insert_data, get_latest_data

app = Flask(__name__)


# ---------------- MQTT ----------------

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to MQTT Broker")
    client.subscribe(MQTT_TOPIC)
    print(f"Subscribed to {MQTT_TOPIC}")


def on_message(client, userdata, msg):

    try:

        payload = msg.payload.decode()

        print(payload)

        data = json.loads(payload)

        insert_data(
            data["distance"],
            data["temperature"],
            data["gas"],
            data["rain"]
        )

    except Exception as e:

        print(e)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)

client.loop_start()


# ---------------- FLASK ----------------

@app.route("/")
def home():

    data = get_latest_data()

    if data is None:
        return "No Data Available"

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
