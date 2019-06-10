import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)


def get_text_from_image(image_url):
    URL = "https://gateway.watsonplatform.net/visual-recognition/api/v3/recognize_text"
    AUTH = ('apikey',config["ibm_visual_recognition"]["apikey"])
    PARAMS = {
        'url':image_url,
        'version':'2018-03-19'
    }
    r = requests.get(url = URL, auth=AUTH, params = PARAMS)
    # extracting data in json format
    data = r.json()
    print(data)
    return data["images"][0]['text']

# a = get_text_from_image('https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/lookButDontTouch.jpg')
# print(a)
