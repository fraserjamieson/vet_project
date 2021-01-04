import unittest
from models.vets import Vetenarian
from models.animals import Animal
from models.customer import Customer

class TestVetenarian(unittest.TestCase):
    def setUp(self):
        self.vet = Vetenarian("Burt")
        self.vet = Vetenarian("Muran")

    def test_vet_has_name(self):
        self.assertEqual(self.vet.name, "Burt")
    
    def test_vet_has_animal(self):
        self.vet.takes_in_animal(self.animal.name)
        self.assertEqual(self.vet.animals[0], "Zero")
