from flask import Flask, request
from flask_mqtt import Mqtt
from twilio.twiml.messaging_response import MessagingResponse
import json
import twilio_messaging as messaging
import chatbot
import db
import connect
# import mqtt_mesh

with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config["mqtt"]["broker"]
app.config['MQTT_BROKER_PORT'] = config["mqtt"]["port"]
# app.config['MQTT_USERNAME'] = 'user'
# app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@app.route("/receive", methods=['GET', 'POST'])
def listen_input():
    message = request.values.get('Body', None)
    from_no = request.values.get('From', None)
    print(message, from_no)

    receiver = db.getReceiver(from_no)
    if receiver == db.IBM_RECEIVER:
        if connect.is_connect_requested(message):
            connect.connect(from_no, message)
            return str(MessagingResponse())
        reply = chatbot.handle_message(from_no, message)
        """Respond to incoming messages with a friendly SMS."""
        # Start our response
        resp = MessagingResponse()
        # Add a messag
        resp.message(reply)
        return str(resp)
    else:
        if connect.is_stop_requested(message):
            connect.disconnect(from_no, receiver)
            return str(MessagingResponse())
        messaging.send_message(receiver, message)
        return str(MessagingResponse())

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.unsubscribe_all()
    mqtt.subscribe('sparrow_receive/+')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    # print(data)
    message = data["payload"]
    from_no = data["topic"].split("/")[1]
    print(message, from_no)

    receiver = db.getReceiver(from_no)
    print(receiver)
    if receiver == db.IBM_RECEIVER:
        if connect.is_connect_requested(message):
            connect.connect(from_no, message)
            return
        print("")
        reply = chatbot.handle_message(from_no, message)
        """Respond to incoming messages with a friendly SMS."""
        # Send our response
        # reply = "Hello again"
        print(reply)
        mqtt.publish(data["topic"].replace("receive", "response"), reply)
        return
    else:
        if connect.is_stop_requested(message):
            connect.disconnect(from_no, receiver)
            return
        messaging.send_message(receiver, message)
        return



if __name__ == "__main__":
    app.run(debug=False)
