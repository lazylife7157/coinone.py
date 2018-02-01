from coinone.api.public import PublicClient
import coinone.api.v1.account as accountv1
import coinone.api.v1.order as orderv1
import coinone.api.v1.transaction as transactionv1
import coinone.api.v2.account as accountv2
import coinone.api.v2.order as orderv2
import coinone.api.v2.transaction as transactionv2

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
