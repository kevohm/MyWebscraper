from Webscraper import Webscraper

if __name__ == "__main__":
    url = "https://afx.kwayisi.org/nse/"
    obj = Webscraper()
    obj.fetchData(url).read_data().extract_data().saveToFile()