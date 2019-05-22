import json
import pymongo
import chatbot
from datetime import datetime

TYPE_USER = 'user'
TYPE_DOCTOR = 'doctor'
TYPE_COMMUNITY = 'community'
IBM_RECEIVER = 'ibm_assistant'

with open('config.json') as config_file:
    config = json.load(config_file)


myclient = pymongo.MongoClient(config["mongo"]["client"])
mydb = myclient["sparrow"]
sessionCol = mydb["sessions"]
userCol = mydb["users"]

def getSessionID(userID):
    user = sessionCol.find_one({"userID":userID})
    print(user)
    if user:
        print(user)
        return user['sessionID']
    else:
        session = chatbot.new_session()
        my_dic = {'userID':userID, 'sessionID':session, 'created_at': datetime.utcnow()}
        sessionCol.insert_one(my_dic)
        return session

def getReceiver(userID):
    user = userCol.find_one({"userID":userID})
    if user:
        return user["receiver"]
    else:
        #new user with default to ibm_assistant
        my_dic = {'userID': userID, 'receiver':IBM_RECEIVER, 'type':'user'}
        userCol.insert_one(my_dic)
        return 'ibm_assistant'

def updateUserType(userID, type):
    userCol.update_one({
        'userID':userID
    }, {
        '$set':{
            'type':type
        }
    }, upsert=False)

def setupConnection(user1, user2):
    userCol.update_one({
        'userID':user1
    }, {
        '$set':{
            'receiver':user2
        }
    }, upsert=False)
    userCol.update_one({
        'userID':user2
    }, {
        '$set':{
            'receiver':user1
        }
    }, upsert=False)

def breakConnection(user1, user2):
    userCol.update_one({
        'userID':user1
    }, {
        '$set':{
            'receiver':IBM_RECEIVER
        }
    }, upsert=False)
    userCol.update_one({
        'userID':user2
    }, {
        '$set':{
            'receiver':IBM_RECEIVER
        }
    }, upsert=False)

def findDoctor():
    user = userCol.find_one({'type':TYPE_DOCTOR, 'receiver': IBM_RECEIVER})
    if user:
        return user["userID"]
    else:
        return None

def findCommunity():
    user = userCol.find_one({'type':TYPE_COMMUNITY, 'receiver': IBM_RECEIVER})
    if user:
        return user["userID"]
    else:
        return None
