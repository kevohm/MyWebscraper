from Webscraper import Webscraper
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    url = os.getenv("URL")
    obj = Webscraper()
    obj.fetchData(url).read_data().extract_data().saveToFile()