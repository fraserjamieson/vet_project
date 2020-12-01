import pdb 
from models.animals import Animal
from models.vets import Vetenarian

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animal_repository.delete_all()
vet_repository.delete_all()

halopetcare = Vetenarian("Halo Pet Care")
vet_repository.save(halopetcare)
dolittles = Vetenarian("Do Littles")
vet_repository.save(dolittles)

zero = Animal("Zero", "13/10/2018", "Dog", "01382", "Visited to recieve yearly jab", halopetcare, reece)
animal_repository.save(zero)

beethoven = Animal("Beethoven", "13/11/2018", "Dog", "01382", "Poor thing had soft case of the runs.  Was displaying troubling symptons of something more serious, but aptly treated with relevant antibiotics", halopetcare, reece)
animal_repository.save(beethoven)

luna = Animal("Luna", "12/03/2016", "Parakeet", "0141", "Is lethargic, and wont respond to calling or offering of food.  Possibly a sign of sickness", dolittles)
animal_repository.save(luna)

reece = Customer("Reece")
customer_repository.save(reece)

pdb.set_trace()