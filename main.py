
from lib.angel import AngelLogin
from lib.order import Order

broker = AngelLogin(apikey)

data = broker.generateSession(clientCode=clientcode, password=password)
refreshToken= data['data']['refreshToken']
feedToken=broker.getfeedToken()

symbol = 'SBIN-EQ'
price = '530'
om = Order(broker, symbol)

om.send_order('BUY', '530')
print(broker.orderBook())
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



