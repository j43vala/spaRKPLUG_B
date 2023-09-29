import paho.mqtt.client as mqtt
import sparkplug_b_pb2 as sparkplug

# Define MQTT parameters
MQTT_BROKER_HOST = "192.168.1.10"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "sparkplug/data"

# Define a callback for when the client receives a message
def on_message(client, userdata, message):
    received_payload = sparkplug.Payload()
    received_payload.ParseFromString(message.payload)

    for metric in received_payload.metrics:
        print(f"Name: {metric.name}, Value: {metric.float_value}, Timestamp: {metric.timestamp}")

# Initialize MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

# Set the message callback
client.on_message = on_message

# Subscribe to the MQTT topic
client.subscribe(MQTT_TOPIC)

# Start the MQTT loop to listen for messages
client.loop_forever()
