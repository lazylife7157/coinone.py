from enum import Enum
from ..core import BaseClient, public_get

class Path(Enum):
    OrderBook = 'orderbook/'
    RecentCompleteOrders = 'trades/'
    Ticker = 'ticker/'

class PublicClient(BaseClient):
    def __init__(self):
        super().__init__()

    @public_get(Path.OrderBook)
    def get_order_book(self, currency):
        ...

    @public_get(Path.RecentCompleteOrders)
    def get_recent_complete_orders(self, currency, period):
        ...

    @public_get(Path.Ticker)
    def get_ticker(self, currency):
        ...
