from dotenv import load_dotenv
import os
import json
import requests

from getGoogleUsers import fetch_data_from_api
from google_widget import GoogleWidget

# load the .env file
load_dotenv() 


# print(api_key)  ===> ok

api_key = os.environ.get('Key')
domain = os.environ.get('Domain')


googlewidget = GoogleWidget(domain)

for user in fetch_data_from_api(f"{domain}/api/userswith/google_reviews_api",api_key=api_key):
    user_api_key = user['api_token']
    data = json.loads(user['service_kvpairs'])
    places_id = data['google reviews api']['places_id']
    
    data = googlewidget.get_data(api_key,user_api_key,places_id)

    # print(data)

    fulldata = {
        'user_key': user_api_key,
        'aws_key':api_key,
        'api_data': data
    }

    print(f"{domain}/api/store/google_reviews_api/")

    headers = {'Content-Type': 'application/json'}

    response =  requests.post(f"{domain}/api/store/google_reviews_api/",json=fulldata,headers=headers)

    print(response.text)

googlewidget.close()