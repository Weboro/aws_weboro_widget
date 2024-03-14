#!/usr/bin/python

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

headers = {
    'Content-Type': 'application/json',
}

count = 0
log = "________________________________For Google_____________________________"
print("--------------------------------For Google________________________")

for user in fetch_data_from_api(f"{domain}/api/userswith/google_reviews_api",api_key=api_key):
    count += 1
    
    print(f"For :{count}. {user['name']}")
    log += f"For :{count}. {user['name']}\n"

    user_api_key = user['api_token']
    data = json.loads(user['service_kvpairs'])
    places_id = data['google reviews api']['places_id']
    
    data = googlewidget.get_data(api_key,user_api_key,places_id)

    if data == []:
        print("Error: check for : Invalid placeid")
        log += f"Error: check for - Invalid placeid\n\n"
    else:

        fulldata = {
            'user_key': user_api_key,
            'aws_key':api_key,
            'api_data': data
        }

        # print(f"{domain}/api/store/google_reviews_api/")

        

        response =  requests.post(f"{domain}/api/ssstore/google_reviews_api/",json=fulldata,headers=headers)

        res = response.json()
        print(res)

        log += str(res) + "\n\n"

    print("\n")


googlewidget.close()


log = "________________________________For Tiktok_____________________________"
print("--------------------------------For Tiktok________________________")
count = 0
for user in fetch_data_from_api(f'{domain}/api/userswith/tiktok_api',api_key=api_key):
    count += 1
    
    print(f"For :{count}. {user['name']}")
    log += f"For :{count}. {user['name']}\n"

    user_api_key = user['api_token']

    data = {
        'user_key': user_api_key,
        'key':api_key
    }


    response =  requests.post(f"{domain}/api/ssstore/tiktok_api/",json=data,headers=headers)
    
    if response.status_code != 200:
        log += f"Something went wrong"
        print("Something went wrong")
    else:
        res = response.json()
        print(response.json())
        log += str(res) + "\n\n"
    
    print("\n")




with open('log','w') as file:
    file.write(log)
