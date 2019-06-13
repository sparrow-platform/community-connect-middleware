# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import json
import mqtt_messaging

with open('config.json') as config_file:
    config = json.load(config_file)

MEDIA_SUPPORT_WHATSAPP = ['image/jpeg', 'application/pdf', 'audio/mpeg'] #Supports video/mp4 but needs larger size maybe
MEDIA_SUPPORT_MESSENGER = ['image/jpeg']
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
    elif to_no.startswith('sparrow'):
        mqtt_messaging.send_message(to_no, message)
        return
    else:
        from_no = config["twilio"]["number"]
    message = client.messages.create(
                                  body=message,
                                  from_=from_no,
                                  to=to_no
                              )
    print(message.sid)

def send_message_with_media(sender, to_no, message, media, mime_type):
    from_no = ""
    if to_no.startswith('whatsapp'):
        from_no = config["twilio"]["whatsapp_no"]
        if mime_type not in MEDIA_SUPPORT_WHATSAPP:
            send_message(to_no, message + "\nFollowing media was sent to you: "+ media)
            return
    elif to_no.startswith('messenger'):
        from_no = config["twilio"]["messenger_no"]
        if mime_type not in MEDIA_SUPPORT_MESSENGER:
            send_message(to_no, message + "\nFollowing media was sent to you: "+ media)
            return
    else:
        send_message(to_no, message + "\nFollowing media was sent to you: "+ media)
        return
    message = client.messages.create(
                                  body=message,
                                  from_=from_no,
                                  to=to_no,
                                  media_url=[media]
                              )
    print(message.sid)
