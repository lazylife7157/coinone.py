from .api.public import PublicClient
from .api.v1 import account as accountv1
from .api.v1 import order as orderv1
from .api.v1 import transaction as transactionv1
from .api.v2 import account as accountv2
from .api.v2 import order as orderv2
from .api.v2 import transaction as transactionv2

class Coinone:
    def __init__(self, secret):
        self.__public = PublicClient()
        self.__v1 = V1(secret)
        self.__v2 = V2(secret)

    @property
    def public(self):
        return self.__public

    @property
    def v1(self):
        return self.__v1

    @property
    def v2(self):
        return self.__v2

class V1:
    def __init__(self, secret):
        self.__account = accountv1.AccountClient(secret)
        self.__order = orderv1.OrderClient(secret)
        self.__transaction = transactionv1.TransactionClient(secret)

    @property
    def account(self):
        return self.__account

    @property
    def order(self):
        return self.__order

    @property
    def transaction(self):
        return self.__transaction

class V2:
    def __init__(self, secret):
        self.__account = accountv2.AccountClient(secret)
        self.__order = orderv2.OrderClient(secret)
        self.__transaction = transactionv2.TransactionClient(secret)

    @property
    def account(self):
        return self.__account

    @property
    def order(self):
        return self.__order

    @property
    def transaction(self):
        return self.__transaction
