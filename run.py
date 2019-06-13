from flask import Flask, request, jsonify
from flask_mqtt import Mqtt
from twilio.twiml.messaging_response import MessagingResponse
import json
import twilio_messaging as messaging
import chatbot
import db
import connect
import visual_recognition as vr
import nlp
import os

with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config["mqtt"]["broker"]
app.config['MQTT_BROKER_PORT'] = config["mqtt"]["port"]
# app.config['MQTT_USERNAME'] = 'user'
# app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

cf_port = os.getenv("PORT")

@app.route('/')
def route():
    return "hello ibm new"

@app.route("/middleware/receive", methods=['GET', 'POST'])
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

@app.route("/visual_recognition/text", methods=['POST'])
def recognize_text():
    image_url = request.values.get('image_url', None)
    # print(image_url)
    text = vr.get_text_from_image(image_url)
    #return jsonify({'text':text})
    return text

@app.route("/nlp/sentiment", methods=['POST'])
def sentiment_of_text():
    text = request.values.get('text', None)
    sentiment = nlp.get_sentiment_emotions(text)
    #return jsonify({'text':text})
    return jsonify(sentiment)

@app.route("/nlp/entities", methods=['POST'])
def entities_of_text():
    text = request.values.get('text', None)
    entities = nlp.get_entities(text)
    #return jsonify({'text':text})
    return jsonify(entities)


if __name__ == "__main__":
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)
