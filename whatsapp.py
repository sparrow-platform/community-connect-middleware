# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import json

with open('config.json') as config_file:
    config = json.load(config_file)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = config["twilio"]["account_sid"]
auth_token = config["twilio"]["auth_token"]
client = Client(account_sid, auth_token)

def send_message(message, to_no):
    message = client.messages.create(
                                  body=message,
                                  from_=config["twilio"]["whatsapp_no"],
                                  to=to_no
                              )
    print(message.sid)
