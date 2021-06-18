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
bill = Animal("Bill", "13/10/2018", "Dog", "Visited to recieve yearly jab", muran)
animal_repository.save(bill)
lila = Animal("Lila", "13/10/2018", "Dog", "Visited to recieve yearly jab", muran)
animal_repository.save(lila)

res = customer_repository.select_all()
res2= animal_repository.select_all()

for customer in res:
    print(customer.__dict__)

customer_repository.update(muran)

pdb.set_trace()



