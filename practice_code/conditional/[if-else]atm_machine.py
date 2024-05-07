"""
Simple ATM Machine

ATM
1. withdraw cash, 2. balance info

OCD -- Obsessive compulsive disorder

"""
account_balance = 100

user_input = int(input("Please enter the choice \n 1. For Cash Withdrawal\n 2. For balance Enquiry\n"))

if user_input == 1:
    amount_to_withdraw = int(input('Please enter the amount to withdraw'))
    if amount_to_withdraw <= account_balance:
        print(f'{amount_to_withdraw} is withdrawn')
        account_balance -= amount_to_withdraw
        print(f'{account_balance} is your current account balance')
    else:
        # print("Please restart and enter the amount less than your balance")
        print("Its Ok, see you after salary day")
elif user_input == 2:
    print(f'The Current Account balance is {account_balance}')
else:
    print("Invalid choice, please restart")
