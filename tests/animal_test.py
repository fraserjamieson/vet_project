import unittest
from models.animals import Animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Zero", 2018, "Dog", "01382", "most recent visit: Visited to recieve yearly jab")

    # testing for type of animal by referring to relevant object attribute.

    def test_is_type(self):
        self.assertEqual(self.animal.type, "Dog")