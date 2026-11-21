class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сума поповнення має бути більшою за нуль")
            return
        self.balance += amount
        print(f"Рахунок {self.account_number} поповнено на {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття має бути більшою за нуль")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку")
        else:
            self.balance -= amount
            print(f"З рахунку {self.account_number} знято {amount}. Баланс: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("UA123456", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(5000)