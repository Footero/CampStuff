
class BankAccount:
    def __init__(self, name, balance=5000):
        pass
        
    def deposit(self, amount):
        self.balance = self.balance + alex.deposit
        print("You have " + self.balance + "$ in your account")

    def withdraw(self, amount):
        pass
        
    
    def showAccount(self):
        print("Name: Alex", self.name)
        print("Balance:", self.balance)


def test():
    alex  = BankAccount("Alex")
    bobby = BankAccount("Bobby", 3250)

    # Testing Alex
    assert alex.name == "Alex"
    assert alex.balance == 5000
    alex.deposit(500)
    alex.deposit(1500)
    alex.withdraw(250.25)
    assert alex.balance == 6750.75
    alex.showAccount()

    # Testing Bobby
    assert bobby.name == "Bobby"
    assert bobby.balance == 3250
    bobby.deposit(alex.balance)
    bobby.withdraw(500)
    bobby.withdraw(1250.50)
    assert bobby.balance == 4749.5
    bobby.showAccount()


if __name__ == "__main__":
    test()
    print("Program success!")
