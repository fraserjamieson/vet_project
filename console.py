import pdb 
from models.animal import Animal
from models.customer import Customer

import repositories.animal_repository as animal_repository
import repositories.customer_repository as customer_repository

animal_repository.delete_all()
customer_repository.delete_all()

muran = Customer("Muran Battison", "07957941877")
customer_repository.save(muran)

zero = Animal("Zero", "13/10/2018", "Dog", "Visited to recieve yearly jab", muran)
animal_repository.save(zero)

pdb.set_trace()