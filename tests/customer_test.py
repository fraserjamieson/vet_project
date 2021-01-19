import unittest
from models.animals import Animal
from models.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Muran", "07957941877")

    def test_customer_has_name(self):
        self.assertEqual(self.customer.name, "Muran")
    
    # def test_customer_has_no_name()
    
    def test_customer_has_animal(self):
        self.customer.takes_in_animal(self.animal.name)
        self.assertEqual(self.customer.animals[0], "Zero")

    # def test_customer_has_no_animal

    # def test_customer_has_contact_details

    # def test_customer_has_no_contact_details