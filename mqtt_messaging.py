import paho.mqtt.client as paho
import json

with open('config.json') as config_file:
    config = json.load(config_file)

broker=config["mqtt"]["broker"]
port=config["mqtt"]["port"]

client= paho.Client("sparrow-middleware")
client.connect(broker,port)

def send_message(userID, message):
    topic = "sparrow_response/"+userID
    client.publish(topic,message)
