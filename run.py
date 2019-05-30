from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import twilio_messaging as messaging
import chatbot
import db
import connect

with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
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

if __name__ == "__main__":

    app.run(debug=True)
