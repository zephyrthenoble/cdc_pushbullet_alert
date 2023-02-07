import requests
import json
from config import *

DEBUG = False

pushbullet_endpoint = "https://api.pushbullet.com/v2/pushes"
cdc_endpoint = "https://data.cdc.gov/resource/3nnm-4jni.json"

def main():
    cdc_headers = {"X-App-Token": cdc_access_token}
    pushbullet_header = {"Access-Token": pushbullet_access_token, "Content-Type": "application/json"}
    cdc_query = f"{cdc_endpoint}?county={county}&$order=date_updated DESC&$limit=1"
    print(cdc_query)

    data = requests.get(cdc_query, headers=cdc_headers).json()

    level = data[0]["covid_19_community_level"]
    output = f"COVID community level: {level}"

    print(output)

    if level != "Low" or DEBUG:
        pushbullet_format = {"body": output,
                             "title": "Daily Covid Update",
                             "type": "note"
                             }
        res = requests.post(pushbullet_endpoint, headers=pushbullet_header, data=json.dumps(pushbullet_format))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
