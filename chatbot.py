import json
import ibm_watson

assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='xxxx',
    url='https://gateway.watsonplatform.net/assistant/api'
)

response = assistant.message(
    workspace_id='xxxx',
    input={
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))
