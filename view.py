
def get_initial_menu_choice():
    print('Welcome to Terminal Teller:')
    print('\t1) create account')
    print('\t2) log in')
    print('\t3) quit ')
    selection = input('your choice: ')
    return selection

def get_main_menu_choice(first_name, last_name, account_num):#pass name in from controller
    print(f'Hello,{first_name} {last_name} ({account_num})') #e.g. Hello, Nathan Smith (2345)
    print('\t1) Check balance')
    print('\t2) Withdraw funds')
    print('\t3) Deposit funds')
    print('\t4) sign out')
    selection = input('your choice: ')
    return selection

#option 1
def create_account_prompt():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    pin_a = '0'
    pin_b = '1'
    while pin_a != pin_b:
        pin_a = input("PIN: ")
        pin_b = input("Confirm PIN: ")
        if pin_a == pin_b:
            return first_name, last_name, pin_a
        else:
            print("pins don't match. please try again") #move message to view

def confirm_account_creation(account_num):
    print(f'account created, your account_number is {account_num}')

#option 2
def login_prompt():
    account_num = input("Account number: ")
    pin = input("PIN: ")
    return account_num, pin

#option 3
def confirm_quit():
    print('Goodbye!')

def show_balance(balance):
    print(f"Your balance is ${balance}")

def withdrawal_prompt():
    return input("How much to withdraw: ")

def deposit_prompt():
    return input("How much to deposit: ")