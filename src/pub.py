
class Pub:
    def __init__(self, name, till_value):
        self.name = name
        self.till_value = till_value
        self.drinks = {}

    def drinks_list(self):
        return len(self.drinks)

    def add_money_to_till(self, price):
        self.till_value += price

    def add_drink_to_stock(self, drink):
        if drink in 

    def remove_drink_from_stock(self, drink):
        self.drinks.remove(drink)

    def sell_drink_to_customer(self, drink, customer):
        customer.reduce_wallet(drink.price)
        self.add_money_to_till(drink.price)
        self.remove_drink_from_stock(drink)
        customer.give_customer_drink(drink)

# EXTENSIONS

    def check_customer_age(self, age):
        if age >= 18:
            return True


        
        

    # def sell_drink_to_customer()

        # def sell_pet_to_customer(self, name, customer):
        # pet = self.find_pet_by_name(name)
        # customer.reduce_cash(pet.price)
        # self.increase_total_cash(pet.price)
        # self.increase_pets_sold()
        # self.remove_pet(pet)
        # customer.add_pet(pet)