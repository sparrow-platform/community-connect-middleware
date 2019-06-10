import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, SentimentOptions, EmotionOptions

with open('config.json') as config_file:
    config = json.load(config_file)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey=config["ibm_nlp"]["apikey"],
    url=config["ibm_nlp"]["url"])

def get_sentiment_emotions(input_text):
    response = natural_language_understanding.analyze(
        text=input_text,
        features=Features(
            emotion=EmotionOptions(document=True),
            sentiment=SentimentOptions(document=True)
            )
        ).get_result()
    #print(json.dumps(response, indent=2))
    data = {'sentiment':response["sentiment"]["document"],
            'emotion':response["emotion"]["document"]["emotion"]
        }
    return data
def get_entities(input_text):
    response = natural_language_understanding.analyze(
        text=input_text,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            )).get_result()
    #print(json.dumps(response, indent=2))
    return response["entities"]

# a = get_entities('IBM is an American multinational technology company '
# 'headquartered in Armonk, New York, United States, '
# 'with operations in over 170 countries.')
# print(a)
