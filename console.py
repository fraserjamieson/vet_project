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

reece = Customer("Reece Charity")
customer_repository.save(reece)
muran = Customer("Muran Battison")
customer_repository.save(muran)

zero = Animal("Zero", "13/10/2018", "Dog", "01382", "Visited to recieve yearly jab", halopetcare, reece)
animal_repository.save(zero)

beethoven = Animal("Beethoven", "13/11/2018", "Dog", "01382", "Poor thing had soft case of the runs.  Was displaying troubling symptons of something more serious.  Aptly treated with relevant antibiotics", halopetcare, reece)
animal_repository.save(beethoven)

luna = Animal("Luna", "12/03/2016", "Parakeet", "0141", "Is lethargic, and wont respond to calling or offering of food.  Possibly a sign of sickness", dolittles, muran)
animal_repository.save(luna)

pdb.set_trace()