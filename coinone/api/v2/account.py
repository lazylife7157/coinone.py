from enum import Enum
from ...core import V2Client, v2_request

class Path(Enum):
    Balance = 'balance/'
    DailyBalance = 'daily_balance/'
    DepositAddress = 'deposit_address/'
    UserInformation = 'user_info/'
    VirtualAccount = 'virtual_account/'

class AccountClient(V2Client):
    def __init__(self, secret):
        super().__init__(secret)
        self.uri += 'account/'

    @v2_request(Path.Balance)
    def get_balance(self):
        ...

    @v2_request(Path.DailyBalance)
    def get_daily_balance(self):
        ...

    @v2_request(Path.DepositAddress)
    def get_deposit_address(self):
        ...

    @v2_request(Path.UserInformation)
    def get_user_information(self):
        ...

    @v2_request(Path.VirtualAccount)
    def get_virtual_account(self):
        ...
