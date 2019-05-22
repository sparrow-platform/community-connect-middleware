import json
import ibm_watson
import json
import db

INTENT_DOCTOR = 'Register_Doctor'
INTENT_COMMUNITY = 'Register_Community'

with open('config.json') as config_file:
    config = json.load(config_file)

service = ibm_watson.AssistantV2(
    iam_apikey=config["ibm_assistant"]["iam_apikey"],
    version='2019-02-28',
    url=config["ibm_assistant"]["url"]
)
def handle_message(from_no, message):
    response =  get_response(from_no, message)
    #print(json.dumps(response, indent=2))

    #Handle registration intents
    intent = response["output"]["intents"][0]["intent"]
    if intent == INTENT_DOCTOR:
        db.updateUserType(from_no, db.TYPE_DOCTOR)
    elif intent == INTENT_COMMUNITY:
        db.updateUserType(from_no, db.TYPE_COMMUNITY)
        
    reply = response["output"]["generic"][0]["text"]
    return reply



def get_response(from_no, message):
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
    #reply = response["output"]["generic"][0]["text"]
    #print(reply)
    return response

def new_session():
    response = service.create_session(
        assistant_id=config["ibm_assistant"]["assistant_id"]
    ).get_result()
    print(json.dumps(response, indent=2))
    session = response["session_id"]
    return session
