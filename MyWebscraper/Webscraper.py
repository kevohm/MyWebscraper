from bs4 import BeautifulSoup
import requests
from Formater import Formater
import json

class Webscraper():
    _data = None
    _results = None
    def __init__(self) -> None:
        self._current = None

    def fetchData(self, url):
        print("======== Fetching =======")
        Webscraper._data = requests.get(url).content
        return self
    
    def write_data(self):
        with open("index.html", 'w+') as doc:
            doc.write("{}".format(Webscraper._data))
        return self
    
    def read_data(self):
        with open("index.html", "r") as doc:
            self._current = doc.read()
        return self
    
    def extract_data(self):
        if self._current:
            newObj = Formater()
            newObj.feed(str(self._current))
            Webscraper._results = newObj.data
        return self
    
    def saveToFile(self):
        data = {}
        if Webscraper._results is not None:
            data = Webscraper._results
        with open("data.json", "w") as doc:
            d = json.dumps(data)
            doc.write(d)
    