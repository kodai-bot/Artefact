import requests
import json

# general API method to request data from a resource

def fetch_data_from_api(api_url, api_key=None):
    try:
        params = {"apiKey": api_key}
        response = requests.get(api_url, params=params)

        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
    
    
    # call if u need to parse a json file  
def parse_json(file_to_parse):
    parsed_data = json.loads(file_to_parse)
    return parsed_data

    
    