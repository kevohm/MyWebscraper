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
        print("======== Fetching =======\n\n")
        Webscraper._data = requests.get(url).content
        return self
    
    def write_data(self):
        print("======== Writting to index.html =======\n\n")
        with open("index.html", 'w+') as doc:
            doc.write("{}".format(Webscraper._data))
        return self
    
    def read_data(self):
        print("======== Reading from index.html =======\n\n")
        with open("index.html", "r") as doc:
            self._current = doc.read()
        return self
    
    def extract_data(self):
        print("======== Converting data =======\n\n")
        if self._current:
            newObj = Formater()
            newObj.feed(str(self._current))
            Webscraper._results = newObj.data
            print("======== Data Found =======\n{}\n\n".format(newObj.data))
        return self
    
    def saveToFile(self):
        print("======== Writting data to data.json =======\n\n")
        data = {}
        if Webscraper._results is not None:
            data = Webscraper._results
        with open("data.json", "w") as doc:
            d = json.dumps(data)
            doc.write(d)
    