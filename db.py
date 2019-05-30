import json
import chatbot
from datetime import datetime
from cloudant.client import Cloudant

TYPE_USER = 'user'
TYPE_DOCTOR = 'doctor'
TYPE_COMMUNITY = 'community'
IBM_RECEIVER = 'ibm_assistant'

with open('config.json') as config_file:
    config = json.load(config_file)
    
client = Cloudant.iam(config["couch"]["username"], config["couch"]["api"], connect=True)
sessionsDB = client['sessions']
usersDB = client['users']


def getSessionID(userID):
    if userID in sessionsDB:
        return sessionsDB[userID]['sessionID']
    else:
        session = chatbot.new_session()
        my_dic = {'_id':userID, 'sessionID':session, 'created_at': str(datetime.utcnow())}
        sessionsDB.create_document(my_dic)
        return session
   


def getReceiver(userID):
    if userID in usersDB:
        return usersDB[userID]["receiver"]
    else:
        my_dic = {'_id': userID, 'receiver':IBM_RECEIVER, 'type':'user'}
        usersDB.create_document(my_dic)
        return 'ibm_assistant'


def updateUserType(userID, type):
    if userID in usersDB:
        user = usersDB[userID]
        user['type'] = type
        user.save()
        return True
    return False


def setupConnection(user1, user2):    
    if user1 not in usersDB or user2 not in usersDB:
        return False
    userDoc1 = usersDB[user1]
    userDoc1['receiver'] = user2
    userDoc1.save()
    userDoc2 = usersDB[user2]
    userDoc2['receiver'] = user1
    userDoc2.save()
    return True


def breakConnection(user1, user2):
    if user1 not in usersDB or user2 not in usersDB:
        return False
    userDoc1 = usersDB[user1]
    userDoc1['receiver'] = IBM_RECEIVER
    userDoc1.save()
    userDoc2 = usersDB[user2]
    userDoc2['receiver'] = IBM_RECEIVER
    userDoc2.save()
    return True


def findDoctor():
    #TODO Check if self is not returned
    for user in usersDB:
        if user['type'] == TYPE_DOCTOR and user['receiver'] == IBM_RECEIVER:
            return user['_id']
    return None


def findCommunity():
    for user in usersDB:
        if user['type'] == TYPE_COMMUNITY and user['receiver'] == IBM_RECEIVER:
            return user['_id']
    return None

