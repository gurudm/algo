from smartapi import SmartConnect

class AngelLogin(SmartConnect):

    def __init__(self, apikey):
        super().__init__(api_key=apikey)

    def getCandleData(self, **kwargs):
        historicParam = {
            "exchange": "NSE",
            "symboltoken": "3045",
            "interval": "ONE_MINUTE",
            "fromdate": "2021-02-08 09:00",
            "todate": "2021-02-08 09:16"
        }
        return super().getCandleData(historicParam)




