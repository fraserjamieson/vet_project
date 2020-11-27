class Vet:

    def __init__(self, name, id= None):
        self.name = name
        self.animals = []
        self.id = id

    def takes_in_animal(self, animal):
        self.animals.append(animal)
