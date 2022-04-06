import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Black Bull", 1000)
        self.customer_1 = Customer("Dave", 20, 56)
        self.customer_2 = Customer("Susan", 50, 61)
        self.drink_1 = Drink("Tennants", 5, 10,5)
        self.drink_2 = Drink("White Wine", 10, 1, 15)

    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    #@unittest.skip("Delete this line to run the test")
    def test_till_value_total(self):
        self.assertEqual(1000, self.pub.till_value)

    #@unittest.skip("Delete this line to run the test")
    def test_return_list_of_drinks(self):
        self.assertEqual(0, self.pub.drinks_list())

    #@unittest.skip("Delete this line to run the test")
    def test_increase_till_total(self):
        self.pub.add_money_to_till(5)
        self.assertEqual(1005, self.pub.till_value)

    #@unittest.skip("Delete this line to run the test")
    def test_add_drink_to_stock(self):
        self.pub.add_drink_to_stock(self.drink_1)
        self.assertEqual(1, self.pub.drinks_list())
    
    #@unittest.skip("Delete this line to run the test")
    def test_remove_drink_from_stock(self):
        self.pub.add_drink_to_stock(drink_1)
        self.pub.remove_drink_from_stock()
        self.assertEqual(0, self.pub.drinks_list())

    #@unittest.skip("Delete this line to run the test")
    def test_sell_drink_to_customer(self):
        
        drink = Drink("Tennents", 10)
        self.pub.add_drink_to_stock(drink)
        self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(40, customer.wallet)
        self.assertEqual(1010, self.pub.till_value)
        self.assertEqual(0, self.pub.drinks_list())
        self.assertEqual(1, customer.customer_drinks())

# EXTENSION

    @unittest.skip("Delete this line to run the test")
    def test_check_age(self):
        customer_age = 56
        self.pub.check_customer_age(customer_age)
        self.assertEqual(True, self.pub.check_customer_age)


