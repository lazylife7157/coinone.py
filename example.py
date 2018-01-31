#!/usr/bin/python
from pprint import pprint
from coinone import Coinone
from coinone.params import *

if __name__ == '__main__':
    api = Coinone('secret.json')
    pprint(api.v2.account.get_balance())
    pprint(api.public.get_order_book(currency=Currency.XRP))
