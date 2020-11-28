import pdb 
from models.animals import Animal
from models.vets import Vetenarian

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

burt = Vetenarian("Burt")
vet_repository.save(burt)
muran = Vetenarian("Muran")
vet_repository.save(muran)

zero = Animal("Zero", 2018, "Dog", "01382", "Visited to recieve yearly jab")
animal_repository.save(zero)

beethoven = Animal("Beethoven", 2018, "Dog", "01382", "Poor thing had soft case of the runs.  Was displaying troubling symptons of something more serious, but aptly treated with relevant antibiotics")
animal_repository.save(beethoven)

pdb.set_trace()