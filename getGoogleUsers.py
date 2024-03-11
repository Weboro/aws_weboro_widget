import requests



def fetch_data_from_api(api_url,api_key):
    api_url += "?key=" + api_key
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle error
        print("Failed to fetch data:", response.status_code)
        return None
    
