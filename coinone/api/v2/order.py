from enum import Enum
from ...core import V2Client, v2_request

class Path(Enum):
    CancelOrder = 'cancel/'
    LimitBuy = 'limit_buy/'
    LimitSell = 'limit_sell/'
    MyCompleteOrders = 'complete_orders/'
    MyLimitOrders = 'limit_orders/'
    MyOrderInformation = 'order_info/'

class OrderClient(V2Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'order/'

    @v2_request(Path.CancelOrder)
    def cancel_order(self, order_id, price, qty, is_ask, currency):
        ...

    @v2_request(Path.LimitBuy)
    def limit_buy(self, price, qty, currency):
        ...

    @v2_request(Path.LimitSell)
    def limitSell(self, price, qty, currency):
        ...

    @v2_request(Path.MyCompleteOrders)
    def get_my_complete_orders(self, currency):
        ...

    @v2_request(Path.MyLimitOrders)
    def get_my_limit_orders(self, currency):
        ...

    @v2_request(Path.MyOrderInformation)
    def get_my_order_information(self, order_id, currency):
        ...
