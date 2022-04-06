import unittest

#from src.pub import Pub
#from src.drink import Drink 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 20, 56)

    #@unittest.skip("Delete this line to run the test")

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)

    #@unittest.skip("Delete this line to run the test")
    def test_wallet_total(self):
        self.assertEqual(20, self.customer.wallet)

    #@unittest.skip("Delete this line to run the test")
    def test_reduce_wallet_total(self):
        self.customer.reduce_wallet(5)
        self.assertEqual(15, self.customer.wallet)

    #@unittest.skip("Delete this line to run the test")
    def test_can_customer_get_drink(self):
        self.assertEqual(0, self.customer.customer_drinks())

    #@unittest.skip("Delete this line to run the test")
    def test_give_drink_to_customer(self):
        self.customer.give_customer_drink("Tennents")
        self.assertEqual(1, self.customer.customer_drinks())

# EXTENSION

    #@unittest.skip("Delete this line to run the test")
    def test_customer_age(self):
        self.assertEqual(56, self.customer.age)

