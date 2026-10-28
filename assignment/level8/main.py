from BankAccount import BankAccount

print("Welcome to the Bank of Zehao!")

customer_name = input("Please enter your name:\n")
account = BankAccount(customer_name)

option = "5"

def make_deposit(account):
    deposit_amount = float(input("How much would you like to deposit?\n"))
    account.deposit(deposit_amount)

def make_withdrawal(account):
    withdraw_amount = float(input("How much would you like to withdraw?\n"))
    account.withdraw(withdraw_amount)

def view_account_information(account):
    account.account_statement()

while option != "4":
    print("Please choose an option: ")
    print("1. Make a deposit\n2. Make a withdrawal\n3. View account information\n4. Quit")
    option = input("")
    while option not in ['1','2','3','4']:
        option = input("Invalid choice. Please try again.\n")
    if option == '1':
        make_deposit(account)
    elif option == '2':
        make_withdrawal(account)
    elif option == '3':
        view_account_information(account)
                
    

