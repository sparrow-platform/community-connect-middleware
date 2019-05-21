# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACxxxx'
auth_token = 'xxxx'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Let me know if this message reaches you',
                              from_='whatsapp:+14xxxx',
                              to='whatsapp:+91xxxx'
                          )

print(message.sid)
