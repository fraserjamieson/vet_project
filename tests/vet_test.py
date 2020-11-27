import unittest
from models.vet import Vet
from models.animal import Animal

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Halo Pet Care")
        self.animal = Animal("Zero", "31/10/2018", "Dog", 1121, "most recent visit: Visited to receive yearly jab")
    
    def test_vet_has_no_id(self):
        self.assertIsNone(self)
    def test_vet_has_name(self):
        self.assertEqual(self.vet.name, "Halo Pet Care")
        