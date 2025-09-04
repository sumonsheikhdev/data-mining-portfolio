import requests
from src.utils.headers import get_headers

class BaseScraper:
    def __init__(self, url ):
        self.url = url
    

    def fetchUrl(self):
        url = self.url
        response = requests.get(url, headers=get_headers())
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed {url} with status code {response.status_code}")
            return None
        
    def run(self):
        raise NotImplementedError("Each scraper must implement run()")
        

