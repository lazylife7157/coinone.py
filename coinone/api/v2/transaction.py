from enum import Enum
from ...core import V2Client, v2_request

class Path(Enum):
    TwoFactorAuthentication = 'auth_number/'
    CoinTransactionsHistory = 'history/'
    KRWTransactionsHistory = 'krw/history/'

class TransactionClient(V2Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'transaction/'

    @v2_request(Path.TwoFactorAuthentication)
    def get_two_factor_authentication(self, auth_type):
        ...

    @v2_request(Path.CoinTransactionsHistory)
    def get_coin_transactions_history(self, currency):
        ...

    @v2_request(Path.KRWTransactionsHistory)
    def get_krw_transactions_history(self):
        ...
