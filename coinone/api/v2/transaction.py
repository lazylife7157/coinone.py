from enum import Enum
from ...core import V2Client, v2_post

class Path(Enum):
    TwoFactorAuthentication = 'auth_number/'
    CoinTransactionsHistory = 'history/'
    KRWTransactionsHistory = 'krw/history/'

class TransactionClient(V2Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'transaction/'

    @v2_post(Path.TwoFactorAuthentication)
    def get_two_factor_authentication(self, auth_type):
        ...

    @v2_post(Path.CoinTransactionsHistory)
    def get_coin_transactions_history(self, currency):
        ...

    @v2_post(Path.KRWTransactionsHistory)
    def get_krw_transactions_history(self):
        ...
