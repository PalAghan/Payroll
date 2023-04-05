class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        return amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount
        
    def check_balance(self):
        print(f"Account balance: {self.balance}")
        
    def customer_details(self):
        print(f"Customer name: {self.customer_name}")
        print(f"Account number: {self.account_number}")
        print(f"Date of account opening: {self.date_of_opening}")
        print(f"Account balance: {self.balance}")

my_account = BankAccount("1987654321", 1000, "2023-03-01", "Leo G.O.A.T Messi")

deposited_amount = my_account.deposit(2000)
print(f"Amount deposited: {deposited_amount}")

withdrawn_amount = my_account.withdraw(450)
if withdrawn_amount == "Insufficient balance":
    print("Unable to withdraw amount, insufficient balance")
else:
    print(f"Withdrawn amount: {withdrawn_amount}")


my_account.check_balance()

my_account.customer_details()

