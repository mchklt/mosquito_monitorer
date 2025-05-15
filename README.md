# mosquito_monitorer
`mosquito_monitorer` is a lightweight Python script that connects to an MQTT broker, listens to all topics, filters out irrelevant messages (specifically those with a payload length of exactly 29), and logs only meaningful data into a timestamped text file.
