import paho.mqtt.client as paho
import json

with open('config.json') as config_file:
    config = json.load(config_file)

broker=config["mqtt"]["broker"]
port=config["mqtt"]["port"]


def send_message(userID, message):
    client= paho.Client("sparrow-middleware")
    client.connect(broker,port)
    topic = "sparrow_response/"+userID
    ret  = client.publish(topic,message)
    print(ret, topic, message)
    client.disconnect()
