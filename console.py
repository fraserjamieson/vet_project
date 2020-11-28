import pdb 
from models.animals import Animal
from models.vets import Vetenarian

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

burt = Vetenarian("Burt")
vet_repository.save(burt)
muran = Vetenarian("Muran")
vet_repository.save(muran)

# animal_1 = Animal("Zero", 2018, "Dog", "01382", "most recent visit: Visited to recieve yearly jab")

# animal_2 = Animal("Beethoven", 2018, "Dog", 1131, "most recent visit: Poor thing had soft case of the runs.  Was displaying troubling symptons of something more serious, but aptly treated with relevant antibiotics")

pdb.set_trace()