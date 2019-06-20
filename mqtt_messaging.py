import requests
import json
import os
from time import sleep
with open('config.json') as config_file:
    config = json.load(config_file)

URL = "http://localhost:"

cf_port = os.getenv("PORT")
if cf_port == None:
    URL+=str(5000)
else:
    URL+=str(cf_port)

URL+= "/mqtt/publish"

def send_message(userID, message):
    topic = "sparrow_response/"+userID
    PARAMS = {
        'topic':topic,
        'message': message
    }
    print("making request", URL)
    r = requests.post(url = URL, params = PARAMS)
    data = r.json()
    print(data)
