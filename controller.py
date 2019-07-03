#!usr/bin/env python3

#July 2 -- build out view and controller and use model


import view as v
from model import Account

def start():
	while True:
			selection = v.get_initial_menu_choice()
			print(f'this was the selection: {selection}')
		#is it better to test for quit first or go in same order as menu?
			if int(selection)==1: #create account
				first_name, last_name, pin = v.create_account_prompt()
				account=Account()
				account_num = account.create_account(first_name, last_name, pin)
				#account.save() #FIXME
				v.confirm_account_creation(account_num)
			elif int(selection)==2: #login
				account_num, pin = v.login_prompt()
				authenticated_user= Account.login(account_num, pin)
				#if the login is successful -- validated by model show next menu
				while authenticated_user:
					selection = v.get_main_menu_choice(
								authenticated_user.first_name, 
								authenticated_user.last_name,
								authenticated_user.account_num)
					if int(selection)==1: #check balance
						v.show_balance(authenticated_user.get_balance())
					elif int(selection)==2: #withdraw
						amount = v.withdrawal_prompt()
						authenticated_user.withdraw(amount)
						authenticated_user.save()
					elif int(selection)==3: #deposit
						amount = v.deposit_prompt()
						authenticated_user.deposit(amount)
						authenticated_user.save()
					elif int(selection)==4: #quit
						v.confirm_quit()
						break

			elif int(selection)==3:
				v.confirm_quit()
				break
		

	def create_account():
		pass


if __name__=='__main__':
    start()