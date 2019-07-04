import json
import db
import twilio_messaging as messaging

def is_connect_doctor(message):
    if message.lower() == "connect to doctor":
        return True
    return False

def is_connect_community(message):
    if message.lower() == "connect to community":
        return True
    return False

def is_connect_requested(message):
    return (is_connect_doctor(message) or is_connect_community(message))

def connect(userID, message):
    if is_connect_doctor(message):
        doctor = db.findDoctor(userID)
        if doctor:
            db.setupConnection(userID, doctor)
            messaging.send_message(userID, "We have connected you to a doctor")
            messaging.send_message(doctor, "We have connected you to a user")
        else:
            messaging.send_message(userID, "No doctors are available")
    elif is_connect_community(message):
        community = db.findCommunity(userID)
        if community:
            db.setupConnection(userID, community)
            messaging.send_message(userID, "We have connected you to a member")
            messaging.send_message(community, "We have connected you to a user")
        else:
            messaging.send_message(userID, "No members are available")

def connect_expert(userID, type):
    expert = db.findExpert(userID, type)
    if expert:
        db.setupConnection(userID, expert)
        messaging.send_message(userID, "We have connected you to a "+type)
        messaging.send_message(expert, "We have connected you to a user")
    else:
        messaging.send_message(userID, "No "+type+" is available")
    return expert

def is_stop_requested(message):
    if message.lower() == "disconnect":
        return True
    return False

def disconnect(user1, user2):
    db.breakConnection(user1, user2)
    messaging.send_message(user1, "You have been disconnected")
    messaging.send_message(user2, "The other party disconnected")
