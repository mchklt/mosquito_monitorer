# mosquito_monitorer

`mosquito_monitorer` is a Python script that connects to an MQTT broker, subscribes to all topics, filters out payloads with length exactly 29 characters, and logs only meaningful messages.

## Features

- Connects to any MQTT broker provided as a command-line argument
- Subscribes to all MQTT topics (`#`)
- Filters out fixed-length messages (e.g., heartbeats)
- Logs timestamp, topic, payload length, and content
- Saves filtered messages to `mqtt_logs_filtered.txt`
- Displays log events in real time

## Requirements

- Python 3.x
- `paho-mqtt` library

Install it via pip:

```bash
pip install paho-mqtt
````

## Usage

Run the script and provide your MQTT broker address as the first argument:

```bash
python mosquito_monitorer.py <broker>
```

i prefer use it with nohup 

```bash
nohup python mosquito_monitorer.py <broker> &
```
Example:

```bash
nohup python mosquito_monitorer.py broker.hivemq.com &
```

If no broker is specified, the script will exit with a usage message.

## Output

Filtered messages are saved to `mqtt_logs_filtered.txt` like so:

```
[2025-05-15 12:30:45] Topic: sensor/data | Length: 34
{"temperature": 21.5, "humidity": 42}
```

## Tips & Tricks for MQTT Pentesting

* Use `mosquitto_sub` to quickly subscribe to all topics:

  ```bash
  mosquitto_sub -h <broker> -t '#' -v
  ```

* Use `mosquitto_pub` to send test messages:

  ```bash
  mosquitto_pub -h <broker> -t 'topic/test' -m 'your message'
  ```

* Filter out fixed-length heartbeat messages to focus on useful data.

* Check for retained messages with `mosquitto_sub -r`.

* Verify if the broker allows anonymous connections or requires authentication.

Mastering MQTT means seeing beyond noise spotting the real signals hiding in the chatter. With tools like `mosquito_monitorer` and `mosquitto_sub`, you can unveil secrets, test defenses, and control the invisible data streams powering today’s connected world. Stay curious, stay sharp, and hack responsibly.
