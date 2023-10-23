import requests
import json



class APIHandler:  
    def __init__(self):
        pass
    
    # general API method to request data from a resource

    def fetch_data_from_api(self, api_url, api_key):
        try:
            params = {"apiKey": api_key}
            response = requests.get(api_url, params=params)

            response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
            data = response.json()
            print(f"Data fetched from {api_url}.")
            print(f"Number of results: {len(data['results'])}")
            print(f"Results: {data['results']}")
            return data
    
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None
    



# Json handler class to parse and save json data

class JSONHandler:
    def __init__(self):
        pass
    
    # call if u need to parse a json file  
    def parse_json(file_to_parse):
        parsed_data = json.loads(file_to_parse)
        return parsed_data
    
    
    # call if u need to save json data to a local file
    def save_data_to_file(self, data, path):
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            print(f"Data saved to {path}.")

    
    

    
    # 


    
    