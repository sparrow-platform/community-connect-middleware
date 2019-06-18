import connect
import db
import twilio_messaging as messaging

def is_sparrow_request(message):
    if message.startswith("@sparrow"):
        return True
    else:
        return False

def handle_sparrow_request(from_no, message):
    new_message = message.split(' ', 1)[1].strip() # Remove first word (@sparrow here)
    receiver = db.getReceiver(from_no)
    if connect.is_connect_requested(new_message):
        if receiver == db.IBM_RECEIVER:
            connect.connect(from_no, new_message)
        else:
            messaging.send_messages(from_no, ["You are already connected to a sparrow agent.","To disconnect first message\n@sparrow disconnect"])
    elif connect.is_stop_requested(new_message):
        if receiver != db.IBM_RECEIVER:
            connect.disconnect(from_no, receiver)
        else:
            messaging.send_messages(from_no, ["You are not connected to any sparrow agent.","To connect first message\n@sparrow connect doctor/community"])
    elif new_message.strip() == "help":
        messaging.send_messages(from_no, ["Sparrow is here to help you", "Use @sparrow to send sparrow commands\n\"@sparrow connect to doctor\" \tConnects you to doctor\n\"@sparrow connect to community\" \tConnects you to community\n\"@sparrow disconnect\" \tDisconnects you\n"])
    else:
        messaging.send_message(from_no, "We cannot understand your command.\nMessage @sparrow help to get the commands")
