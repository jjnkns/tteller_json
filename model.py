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
    def __init__(self, account_num="", 
                 pin="",balance=0, first_name ="", last_name =""):
        # populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name
        self.data = {}
        self.load()

    def create_account(self, first_name, last_name, pin):
        while True: #consider improving while loop condition
            num = random.randint(100000,999999) 
            customer_account = str(num)
            if customer_account not in self.data:
                self.first_name = first_name
                self.last_name = last_name
                self.pin = pin
                self.balance = 0
                self.account_num = customer_account
                self.data.update({self.account_num: {"pin" : self.pin, 
                "balance": self.balance, 
                "first": self.first_name, 
                "last": self.last_name}})
               
                return customer_account
                
    def load_accounts(self):
        try:
            with open(self.data_path) as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass
    #add new account to dictionary if it doesn't already exist
    def save_account(self):
        self.data.update({
            self.account_num:
            {
                    "pin" : self.pin, 
                    "balance": self.balance, 
                    "first": self.first_name, 
                    "last": self.last_name
            }
        })
       

    def load_file(self):
        try:
            with open(self.data_path) as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass

    def load(self):
        try:
            with open(self.data_path) as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass

        
    #need to write a function that will merge dictionary loaded from json file and dictionary for new accoiunts

    def save_file(self):
        # update the json file with this account's data. data {} will have one or more accounts
        #print(json.dumps(self.data, indent=2))
        try:
            with open(self.data_path, 'w') as json_file:
                json.dump(self.data,json_file, indent=2)
        except FileNotFoundError:
            print("can't find file")

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        # increase the balance of this account
        self.balance+=float(amount)
        return self.balance

    def withdraw(self, amount):
        if float(amount) <= self.balance:
            self.balance-=float(amount)
            return self.balance
        else:
            print("Insufficient Funds")
        # decrease the balance of this account
        # raise ValueError if there are insufficient funds or create an
        # InsufficientFunds exception type    
   
    def login(self, account_num, pin):
        if account_num in self.data:
            if self.data[account_num]['pin']==pin:
                self.account_num = account_num
                self.pin = self.data[account_num]['pin']
                self.balance = self.data[account_num]['balance']
                self.first_name = self.data[account_num]['first']
                self.last_name = self.data[account_num]['last']
                return self
            else:
                return None


