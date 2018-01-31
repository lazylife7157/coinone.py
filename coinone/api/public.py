from enum import Enum
from ..core import BaseClient, public_request

class Path(Enum):
    OrderBook = 'orderbook/'
    RecentCompleteOrders = 'trades/'
    Ticker = 'ticker/'

class PublicClient(BaseClient):
    def __init__(self):
        super().__init__()

    @public_request(Path.OrderBook)
    def get_order_book(self, currency):
        ...

    @public_request(Path.RecentCompleteOrders)
    def get_recent_complete_orders(self, currency, period):
        ...

    @public_request(Path.Ticker)
    def get_ticker(self, currency):
        ...
