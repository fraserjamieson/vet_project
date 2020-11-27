import unittest
from models.vet import Vet
from models.animal import Animal

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Halo Pet Care")
        self.animal = Animal("Zero", 2018, "Dog", "01382", "most recent visit: Visited to recieve yearly jab")

    def test_vet_has_name(self):
        self.assertEqual(self.vet.name, "Halo Pet Care")
    
    def test_vet_has_animal(self):
        self.vet.takes_in_animal(self.animal.name)
        self.assertEqual(self.vet.animals[0], "Zero")
