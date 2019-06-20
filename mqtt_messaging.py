
import paho.mqtt.publish as publish
import requests
import json
import os
from time import sleep
with open('config.json') as config_file:
    config = json.load(config_file)

mqttPublishBroker=config["mqtt"]["broker"]
mqttPublishPort=config["mqtt"]["port"]

cf_port = os.getenv("PORT")

def send_message(userID, message):
    topic = "sparrow_response/"+userID
    publish.single(topic, message, hostname=mqttPublishBroker)
    
