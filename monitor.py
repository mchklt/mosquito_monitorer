import paho.mqtt.client as mqtt
from datetime import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python mosquito_monitorer.py <host>")
    sys.exit(1)

BROKER = sys.argv[1]
TOPIC = "#"
OUTPUT_FILE = "mqtt_logs_filtered.txt"

def on_connect(client, userdata, flags, rc):
    print(f"[+] Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8', errors='ignore')
    if len(payload) != 29:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"[{timestamp}] Topic: {msg.topic} | Length: {len(payload)}\n{payload}\n\n")
        print(f"[LOGGED] Topic: {msg.topic} | Length: {len(payload)}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_forever()
