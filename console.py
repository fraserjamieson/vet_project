import pdb 
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.customer_repository as customer_repository

animal_repository.delete_all()
vet_repository.delete_all()
customer_repository.delete_all()

halopetcare = Vetenarian("Halo Pet Care")
vet_repository.save(halopetcare)
dolittles = Vetenarian("Do Littles")
vet_repository.save(dolittles)

vet_repository.select_all()

muran = Customer("Muran Battison")
customer_repository.save(muran)

zero = Animal("Zero", "13/10/2018", "Dog", "01382", "Visited to recieve yearly jab", halopetcare, reece)
animal_repository.save(zero)

pdb.set_trace()