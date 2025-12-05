# Q1. Create a BankAccount class with attributes account_number, owner_name, and balance.

# Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
    def __str__(self):
        return(f"{self.owner_name} has {self.balance} rupees")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient balance")
    
    def check_Balance(self):
        print(f"Current Balance : {self.balance}")

acc1 = BankAccount(202, "Suhani", 500)
acc1.deposit(200)
print(acc1)
acc1.check_Balance()

acc2 = BankAccount(202, "Amit", 500)
acc2.withdraw(200)
print(acc2)
acc2.check_Balance()