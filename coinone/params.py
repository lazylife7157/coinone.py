from enum import Enum


ACCESS_TOKEN = 'access_token'
SECRET_KEY = 'secret_key'
NONCE = 'nonce'

class Currency(Enum):
    DEFAULT = 'btc'
    BTC = 'btc'
    BCH = 'bch'
    ETH = 'eth'
    ETC = 'etc'
    XRP = 'xrp'
    QTUM = 'qtum'
    IOTA = 'iota'
    LTC = 'ltc'
    BTG = 'btg'

class Period(Enum):
    DEFAULT = 'hour'
    HOUR = 'hour'
    DAY = 'day'

class AuthType(Enum):
    KRW = 'krw'
    BTC = 'btc'
    BCH = 'bch'
    ETH = 'eth'
    ETC = 'etc'
    XRP = 'xrp'
    QTUM = 'qtum'
    IOTA = 'iota'
    LTC = 'ltc'

class IsAsk(Enum):
    ASK = 1
    BID = 0
