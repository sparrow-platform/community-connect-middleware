from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import ibm_watson
import pymongo

with open('config.json') as config_file:
    config = json.load(config_file)


service = ibm_watson.AssistantV2(
    iam_apikey=config["ibm_assistant"]["iam_apikey"],
    version='2019-02-28',
    url=config["ibm_assistant"]["url"]
)
myclient = pymongo.MongoClient(config["mongo"]["client"])
mydb = myclient["sparrow"]
mycol = mydb["sessions"]

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def listen_input():
    message = request.values.get('Body', None)
    from_no = request.values.get('From', None)
    print(message, from_no)
    session = getSessionID(from_no)
    response = service.message(
        assistant_id=config["ibm_assistant"]["assistant_id"],
        session_id=session,
        input={
            'message_type': 'text',
            'text': message
        }
    ).get_result()
    #print(json.dumps(response, indent=2))
    #res = json.dumps(response)
    reply = response["output"]["generic"][0]["text"]
    print(reply)
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a messag
    resp.message(reply)

    return str(resp)



def getSessionID(userID):
    user = mycol.find_one({"userID":userID})
    print(user)
    if user:
        print(user)
        return user['sessionID']
    else:
        response = service.create_session(
            assistant_id=config["ibm_assistant"]["assistant_id"]
        ).get_result()
        print(json.dumps(response, indent=2))
        session = response["session_id"]

        my_dic = {'userID':userID, 'sessionID':session}
        mycol.insert_one(my_dic)
        return session

if __name__ == "__main__":

    app.run(debug=True)
