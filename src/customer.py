class Customer():
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drinks = []
    
    def reduce_wallet(self, spend):
        self.wallet -= spend

    def customer_drinks(self):
        return len(self.drinks)

    def give_customer_drink(self, drink):
        self.drinks.append(drink)

