from db.run_sql import run_sql

from models.animals import Animal
from models.vets import Vetenarian
import repositories.vet_repository as vet_repository


# CRUD operations 
# create 

def save(animal):
    sql = "INSERT INTO animals (name, dob, animal_type, contact_details, notes, vetenarian_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.animal_type, animal.contact_details, animal.notes, animal.vetenarian.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    return animal

# select

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vetenarian = vet_repository.select(result['vetenarian_id'])
        animal = Animal(result['name'], result['dob'], result['animal_type'],result['contact_details'], result['notes'], result['vetenarian_id'], result['id'])
    return animal

# select all 

def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        vetenarian = vet_repository.select(row['vetenarian_id'])
        animal = Animal(row['name'], row['dob'], row['animal_type'], row['contact_details'], row['notes'], vetenarian, row['id'])
        animals.append(animal)
    return animals

# delete

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete all

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

# update (one)

def update(animal):
    sql = "UPDATE animals SET (name, dob, animal_type, contact_details, notes, vetenarian_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.dob, animal.animal_type, animal.contact_details, animal.notes, animal.vetenarian.id, animal.id]
    print(values)
    run_sql(sql, values)

def display_vet_animals(id):
    vet_animals = []
    sql = """SELECT *
            FROM animals
            WHERE vetenarian_id = %s"""
    values = [id]
    results = run_sql(sql, vaules)
    vetenarian = vet_repository.select(id)
    for result in results:
        animals =  Animal(
        result ["name"],
        result ["dob"], 
        result ["animal_type"], 
        result ["contact_details"],
        result["notes"],
        vetenarian,
        result ["id"])
        vet_animals.append(animals)
    return vet_animals