### Task 19: ATM System
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")


# user input
bal = int(input("Enter initial balance: "))
atm = ATM(bal)

# menu
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        atm.deposit(amt)

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        atm.withdraw(amt)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
