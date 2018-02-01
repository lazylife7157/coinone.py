# coinone.py
Simple coinone api wrapper

## Installation
```sh
$ git clone https://github.com/lazylife7157/coinone.py
$ cd coinone.py
$ sudo pip3 install .
```

## Example
```python
from pprint import pprint
from coinone import Coinone
from coinone.params import *

if __name__ == '__main__':
    api = Coinone('secret.json')
    pprint(api.public.get_order_book(currency=Currency.XRP))
    pprint(api.v1.account.get_balance())
    pprint(api.v2.account.get_balance())
```
