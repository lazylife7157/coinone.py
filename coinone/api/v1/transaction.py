from enum import Enum
from ...core import V1Client, v1_post

class Path(Enum):
    TwoFactorAuthentication = 'auth_number/'
    CoinTransactionsHistory = 'history/'
    KRWTransactionsHistory = 'krw/history/'
    SendBTC = 'btc/'

class TransactionClient(V1Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'transaction/'

    @v1_post(Path.TwoFactorAuthentication)
    def get_two_factor_authentication(self, type):
        ...

    @v1_post(Path.CoinTransactionsHistory)
    def get_coin_transactions_history(self):
        ...

    @v1_post(Path.KRWTransactionsHistory)
    def get_krw_transactions_history(self):
        ...

    @v1_post(Path.SendBTC)
    def send_btc(self, address, auth_number, qty, type, from_address):
        ...
