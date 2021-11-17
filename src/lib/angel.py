from smartapi import SmartConnect

class AngelLogin():

    def __init__(self, clientid, password, apikey):
        self.apikey = apikey
        self.password = password
        self.clientid = clientid

    def login(self):
        handle = SmartConnect(api_key=self.apikey)
        handle.generateSession(clientCode=self.clientid, password=self.password)
        return handle

    def getCandleData(self, **kwargs):
        historicParam = {
            "exchange": "NSE",
            "symboltoken": "3045",
            "interval": "ONE_MINUTE",
            "fromdate": "2021-02-08 09:00",
            "todate": "2021-02-08 09:16"
        }
        return super().getCandleData(historicParam)





