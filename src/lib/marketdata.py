from src.lib import util


class Marketdata:

    def __init__(self, broker, symbol):
        self.broker = broker
        self.symbol = symbol

    def ltp(self):
        stoken = util.get_token(self.symbol)
        return self.broker.ltpData('NSE', self.symbol, stoken)
