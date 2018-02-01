from enum import Enum
from ...core import V1Client, v1_get

class Path(Enum):
    BTCDepositAddress = 'btc_deposit_address/'
    Balance = 'balance/'
    DailyBalance = 'daily_balance/'
    UserInformation = 'user_info/'
    VirtualAccount = 'virtual_account/'

class AccountClient(V1Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'account/'

    @v1_get(Path.BTCDepositAddress)
    def get_btc_deposit_address(self):
        ...

    @v1_get(Path.Balance)
    def get_balance(self):
        ...

    @v1_get(Path.DailyBalance)
    def get_daily_balance(self):
        ...

    @v1_get(Path.UserInformation)
    def get_user_information(self):
        ...

    @v1_get(Path.VirtualAccount)
    def get_virtual_account(self):
        ...
