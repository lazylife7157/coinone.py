from enum import Enum
from ...core import V1Client, v1_post

class Path(Enum):
    CancelOrder = 'cancel/'
    LimitBuy = 'limit_buy/'
    LimitSell = 'limit_sell/'
    MyCompleteOrders = 'complete_orders/'
    MyLimitOrders = 'limit_orders/'

class OrderClient(V1Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'order/'

    @v1_post(Path.CancelOrder)
    def cancel_order(self, order_id, price, qty, is_ask):
        ...

    @v1_post(Path.LimitBuy)
    def limit_buy(self, price, qty):
        ...

    @v1_post(Path.LimitSell)
    def limitSell(self, price, qty):
        ...

    @v1_post(Path.MyCompleteOrders)
    def get_my_complete_orders(self):
        ...

    @v1_post(Path.MyLimitOrders)
    def get_my_limit_orders(self):
        ...
