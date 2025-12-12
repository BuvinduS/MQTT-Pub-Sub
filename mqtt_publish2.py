import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "broker.hivemq.com"

# for debugging
def on_publish(client, userdata, mid, reason_code, properties):
    print("Message delivered", mid)

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="Temperature_outside", protocol=mqtt.MQTTv5)
client.on_publish = on_publish

client.connect(mqttBroker, 1883, 60)
client.loop_start()

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", str(randNumber))
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
