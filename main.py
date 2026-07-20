class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение на {amount}.\nБаланс: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Недостаточно средств")
            return
        
        self.balance -= amount
    
    def show_balance(self):
        print(f"Баланс: {self.balance}")

User1 = BankAccount(owner="Ruslan", balance=10000)
print(User1.balance)

User2 = BankAccount(owner="Vlad", balance=7000)
print(User2.balance)
