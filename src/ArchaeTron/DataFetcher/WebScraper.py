import beautifulsoup4 as bs4
import requests
import json
import os
import re



class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.data = None
        self.text = None
        self.json = None
        self.html = None
        self.file = None

    def get_soup(self):
        try:
            self.soup = bs4.BeautifulSoup(self.text, "html.parser")
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        
        return self.soup
    
    def get_data(self):
        try:
            self.data = self.soup.find_all("div", class_="data")
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        
        return self.data
    
    def get_text(self):
        try:
            self.text = requests.get(self.url).text
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        
        return self.text
    
    def get_json(self):
        try:
            self.json = json.loads(self.text)
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        
        return self.json
    
    def get_html(self):
        try:
            self.html = self.soup.prettify()
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        
        return self.html
    
    # Call if you need to extract json dict from a webpage text
    @staticmethod
    def text_to_json(data):
        data_json = json.loads(data.text)
        return data_json