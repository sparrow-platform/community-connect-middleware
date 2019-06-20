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
import sparrow_handler as sparrow
from time import sleep

import paho.mqtt.publish as publish

with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config["mqtt"]["broker"]
app.config['MQTT_BROKER_PORT'] = config["mqtt"]["port"]
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
# app.config['MQTT_USERNAME'] = 'user'
# app.config['MQTT_PASSWORD'] = 'secret'

mqtt = Mqtt(app)

mqttPublishBroker=config["mqtt"]["broker"]
mqttPublishPort=config["mqtt"]["port"]

flag_connected = 0

cf_port = os.getenv("PORT")

@app.route('/')
def route():
    return "hello ibm new"

@app.route("/middleware/receive", methods=['GET', 'POST'])
def listen_input():
    message = request.values.get('Body', None)
    from_no = request.values.get('From', None)
    print(message, from_no)

    #Handling Media content
    num_media = int(request.values.get("NumMedia"))
    if num_media > 0:
        media_url = request.values.get(f'MediaUrl0')
        mime_type = request.values.get(f'MediaContentType0')
        print(media_url, mime_type)
        if num_media > 1:
            messaging.send_message(from_no, "Multiple media cannot be sent. Sending only first media")

    #Handling @sparrow commands
    if sparrow.is_sparrow_request(message):
        sparrow.handle_sparrow_request(from_no, message)
        return str(MessagingResponse())

    receiver = db.getReceiver(from_no)
    if receiver == db.IBM_RECEIVER:
        if sparrow.is_command(message):
            sparrow.handle_command(from_no, message)
            return str(MessagingResponse())
        elif num_media > 0:
            reply = "Sorry! Our Automated chatbot doesn't support Media at this point."
        elif message == "":
            reply = "Invalid format. Your message is empty!"
        else:
            replies = chatbot.handle_message(from_no, message)
            if len(replies) > 1:
                messaging.send_messages(from_no, replies)
                return(str(MessagingResponse()))
            else:
                reply = replies[0]
        resp = MessagingResponse()
        resp.message(reply)
        return str(resp)
    else:
        if num_media > 0:
            messaging.send_message_with_media(from_no, receiver, message, media_url, mime_type)
        elif message == "":
            messaging.send_message(from_no, "Invalid message. Can't be sent")
        else:
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

    if sparrow.is_sparrow_request(message):
        sparrow.handle_sparrow_request(from_no, message)
        return str(MessagingResponse())

    receiver = db.getReceiver(from_no)
    print(receiver)
    if receiver == db.IBM_RECEIVER:
        if sparrow.is_command(message):
            sparrow.handle_command(from_no, message)
            return str(MessagingResponse())

        reply = chatbot.handle_message(from_no, message)
        for message in reply:
            mqtt.publish(data["topic"].replace("receive", "response"), message)
            sleep(1)
        return
    else:
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

<<<<<<< HEAD
=======
@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        print('Error: {}'.format(buf))


@app.route("/mqtt/publish", methods=['POST'])
def publishMQTT():
    topic = request.values.get('topic', None)
    message = request.values.get('message', None)

    try:
        publish.single(topic, message, hostname=mqttPublishBroker)
        print("API call triggered Publish MQTT publish " , topic, message)
        return jsonify({'success':True})
    except:
        return "{\"message\" : \"Server Error\"}"
    
    
    
>>>>>>> 9b72d6b6f08203e083ce2a3b7d9b381e5b5def6c

if __name__ == "__main__":

    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)

