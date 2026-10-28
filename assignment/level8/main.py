from BankAccount import BankAccount

print("Welcome to the Bank of Zehao!")

customer_name = input("Please enter your name:\n")
account = BankAccount(customer_name, 12345)

option = 5

while option != 4:
    print("Please choose an option: ")
    print("1. Make a deposit\n2. Make a withdrawal\n3. View account information\n4. Quit")
    option = input("")
    while option not in ['1','2','3','4','5']:
        option = input("Invalid choice. Please try again.\n")
    if option == '1':
        deposit_amount = float(input("How much do you want deposit? "))
        BankAccount.deposit(deposit_amount)
    elif option == "2":
        withdraw_amount = float(input("How much you you wanna withdraw? "))
        BankAccount.deposit(withdraw_amount)
    elif option == "3":
        
    

