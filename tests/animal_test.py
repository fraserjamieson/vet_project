import unittest
from models.animal import Animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Zero", 2018, "Dog", "most recent visit: Visited to recieve yearly jab")

    # testing for type of animal by referring to relevant object attribute.

    def test_animal_is_type(self):
        self.assertEqual(self.animal.type, "Dog")
    
    # def test_animal_has_no_type

    # def test_animal_has_name

    # def test_animal_has_no_name

    # def test_animal_has_birthday

    # def test_animal_has_no_birthday

    # def test_animal_has_notes

    # def test_animal_entry_contains_no_notes