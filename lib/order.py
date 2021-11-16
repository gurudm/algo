import json
from lib import angel

SYM = json.loads(open('../data/symbols.json').read())


class Order:
    def __init__(self, broker, symbol):
        self.broker = broker
        self.symbol = symbol

    def send_order(self, ordertype, price):
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": self.symbol,
            "symboltoken": SYM.get(self.symbol),
            "transactiontype": ordertype,
            "exchange": "NSE",
            "ordertype": "LIMIT",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": "1"
        }
        try:
            order_id = self.broker.placeOrder(orderparams)
        except Exception as e:
            print(e)
        else:
            print(order_id)

    def cancel_order(self, order_id):
        self.broker.cancel_order(order_id)

    def amend_order(self): ...
    def order_status(self): ...
    def create_order(self): ...
