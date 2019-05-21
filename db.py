import json
import pymongo
import chatbot
from datetime import datetime

with open('config.json') as config_file:
    config = json.load(config_file)


myclient = pymongo.MongoClient(config["mongo"]["client"])
mydb = myclient["sparrow"]
mycol = mydb["sessions"]

def getSessionID(userID):
    user = mycol.find_one({"userID":userID})
    print(user)
    if user:
        print(user)
        return user['sessionID']
    else:
        session = chatbot.new_session()
        my_dic = {'userID':userID, 'sessionID':session, 'created_at': datetime.utcnow()}
        mycol.insert_one(my_dic)
        return session
