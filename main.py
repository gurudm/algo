import time
from lib.angel import AngelLogin
from lib.order import Order
from lib.marketdata import Marketdata



broker = AngelLogin(clientcode, password, apikey)
brokerapp = broker.login()


symbol = 'BANKNIFTY'
md = Marketdata(brokerapp, symbol)
print('Symbol %s Last traded price : %s' % (symbol, md.ltp()['data']['ltp']))

price = '1'
om = Order(brokerapp, symbol)

om.send_order('BUY', price)
om.order_book(brokerapp)

'''
symbol = "SBIN-EQ"
#ananyse symbol -- predict price, quantity, stoploss
order_manager = Order(broker,symbol)
order_manager.send_order("BUY", 44, 40, 38)


Order Manager:
    input symbol  ex. SBIN - 12345
        Get input symbol
    creates an order
    sends the order
'''

#candledata = broker.getCandleData()

#print(candledata)

'''
lib -- all functions 
data -- csv json
bin -- sh .py
templates  
util -- all utility functions
'''


'''
fuctions
set of functions - package
set of packges - module
'''




