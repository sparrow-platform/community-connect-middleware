import json
import ibm_watson
import json


with open('config.json') as config_file:
    config = json.load(config_file)

assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey=config["ibm_assistant"]["iam_apikey"],
    url=config["ibm_assistant"]["url"]
)

response = assistant.message(
    workspace_id=config["ibm_assistant"]["workspace_id"],
    input={
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))
