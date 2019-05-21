import json
import ibm_watson
import json
import db

with open('config.json') as config_file:
    config = json.load(config_file)

service = ibm_watson.AssistantV2(
    iam_apikey=config["ibm_assistant"]["iam_apikey"],
    version='2019-02-28',
    url=config["ibm_assistant"]["url"]
)

def get_reply(from_no, message):
    session = db.getSessionID(from_no)
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
    return reply

def new_session():
    response = service.create_session(
        assistant_id=config["ibm_assistant"]["assistant_id"]
    ).get_result()
    print(json.dumps(response, indent=2))
    session = response["session_id"]
    return session
