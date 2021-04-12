class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def withdraw(self, amount, description=""):
        if self.checkAmount(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, budget_category):
        if self.checkAmount(amount):
            self.withdraw(amount, f"Transfer to{budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


    def checkAmount(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and food items")
print(food.get_balance())

entertainment = Category("Entertainment")
food.transfer(100.00, entertainment)
entertainment.withdraw(40.00, "Payment for Dstv")


clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

print(food)
print(clothing)
print(entertainment)
