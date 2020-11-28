from db.run_sql import run_sql

from models.animals import Animal
from models.vets import Vetenarian


# create 

def save(animal):
    sql = "INSERT INTO animals (name, DOB, type, contact_details, notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.DOB, animal.type, animal.contact_details, animal.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

# select

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vetenarian = vet_repository.select(result['vetenarian_id'])
        animal = Animal(result['name'], result['DOB'], result['type'], result['contact_details'], result ['notes'], result['id'])
    return animal

# select all 

def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        vetenarian = vet_repository.select(row['vetenarian_id'])
        animal = Animal(row['name'], row['DOB'], row['type'], row['contact_details'], row['notes'], row['id'])
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
    sql = "UPDATE animals SET (name, DOB, type, contact_details, notes, vetenarian_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.DOB, animal.type, animal.contact_details, animal.notes, animal.vetenarian.id, animal.id]
    print(values)
    run_sql(sql, values)