from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import whatsapp
import chatbot
import db

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
        reply = chatbot.get_reply(from_no, message)
        """Respond to incoming messages with a friendly SMS."""
        # Start our response
        resp = MessagingResponse()
        # Add a messag
        resp.message(reply)
        return str(resp)
    else:
        return

if __name__ == "__main__":

    app.run(debug=True)
