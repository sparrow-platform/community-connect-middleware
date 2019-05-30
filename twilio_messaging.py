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

def send_message(to_no, message):
    from_no = ""
    if to_no.startswith('whatsapp'):
        from_no = config["twilio"]["whatsapp_no"]
    elif to_no.startswith('messenger'):
        from_no = config["twilio"]["messenger_no"]
    else:
        from_no = config["twilio"]["number"]
    message = client.messages.create(
                                  body=message,
                                  from_=from_no,
                                  to=to_no
                              )
    print(message.sid)
