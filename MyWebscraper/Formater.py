from html.parser import HTMLParser

class Formater(HTMLParser):
    
    company = ["ABSA","ARM","BAMB","BAT","BKG","BOC","BRIT","CABL","CARB",
    "CGEN","CIC","COOP","CRWN","CTUM","DCON","DTK","EABL","EGAD",
    "EQTY","EVRD","FAHR","FTGH","GLD","HAFR","HBE","HFCK","IMH",
    "JUB","KAPC","KCB","KEGN","KNRE","KPLC","KPLC-P4","KPLC-P7",
    "KQ","KUKZ","KURV","LAPR","LBTY","LIMT","LKL","MSC","NBV",
    "NCBA","NMG","NSE","OCH","ORCH","PORT","SASN","SBIC","SCAN",
    "SCBK","SCOM","SGL","SLAM","SMER","TCL","TOTL","TPSE","UCHM"
    ,"UMME","UNGA","WTK","XPRS"]

    def __init__(self):
        super().__init__()
        self.title = ["Ticker","Name","Volume","Price","Change"]
        self.start = 0
        self.data = []
        self.count = 0
        self.current = ""
        self.obj = {}

    def handle_data(self, info):
        if info == "ABSA":
            self.start = 1
        elif info.startswith("Showing"):
            self.start = 0
        if self.start:
            if self.count < 5:
                self.obj[self.title[self.count]] = info
            if info in Formater.company:
                if self.count < 5:
                    obj = {}
                    obj[self.current] = self.obj
                    self.data.append(obj)
                else:
                    self.count = 0
                    self.obj = {}
                    self.current = info
            else:
                if self.count == 5:
                    obj = {}
                    obj[self.current] = self.obj
                    self.data.append(obj)
            self.count += 1