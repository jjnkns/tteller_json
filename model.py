import json
import os
import random

DIR = os.path.dirname(__file__)
DATAFILENAME = "accounts.json"
DATAPATH = os.path.join(DIR, DATAFILENAME)


class AuthenticationError(Exception):
    pass


class Account:
    data_path = DATAPATH

    def __init__(self, account_num=""):
        # populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = None
        self.balance = 0.0
        self.data = {}
        self.load()
        self.first_name = None
        self.last_name = None
        #use randint for account
        #check to make sure that randint doesn't already exist for another account
    def create_account(self, first_name, last_name, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = 0
        while True:
            num = random.randint(1,100000)
            if num not in self.data:
                self.account_num = num
                return self.account_num
        

    def load(self):
        try:
            with open(self.data_path) as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass

        if self.account_num in self.data:
            self.balance = self.data[self.account_num]["balance"]
            self.pin = self.data[self.account_num]["pin"]

    def save(self):
        # update the json data with this account's data, either creating a new
        # account record or updating an existing one
        try:
            with open(self.data_path, 'w') as json_file:
                self.data[self.account_num]["balance"]=self.balance
                self.data[self.account_num][fir]
                print(json.dumps(self.data))
                json.dump(self.data,json_file)
        except FileNotFoundError:
            print("can't find file")

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        # increase the balance of this account
        self.balance+=float(amount)
        return self.balance

    def withdraw(self, amount):
        if float(amount) < self.balance:
            self.balance-=float(amount)
            return self.balance
        else:
            print("Insufficient Funds")
        # decrease the balance of this account
        # raise ValueError if there are insufficient funds or create an
        # InsufficientFunds exception type    
    @classmethod
    def login(cls, account_num, pin):
        account = cls(account_num)
        if pin != account.pin:
            return None
        return account


# account_num = '000001'
# pin = '1234'
# account = Account.login(account_num, pin)
# print(account.deposit(500))
# print(account.withdraw(3200))
# Account(account_num)
# account.save()
# print(account.balance)

