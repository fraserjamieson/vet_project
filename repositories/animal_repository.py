from db.run_sql import run_sql

from models.animal import Animal
from models.customer import Customer
import repositories.customer_repository as customer_repository


# CRUD operations 

# Create 

def save(animal):
    sql = "INSERT INTO animals (name, dob, animal_type, notes, customer_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.animal_type, animal.notes, animal.customer.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    return animal

# Select

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = customer_repository.select(result['customer_id'])
        animal = Animal(result['name'], result['dob'], result['animal_type'], result['notes'], customer, result['id'])
    return animal

# Select all 

def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        customer = customer_repository.select(row['customer_id'])
        animal = Animal(row['name'], row['dob'], row['animal_type'], row['notes'], customer, row['id'])
        animals.append(animal)
    return animals

# Delete

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Delete all

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

# Update (one)

def update(animal):
    sql = "UPDATE animals SET (name, dob, animal_type, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.dob, animal.animal_type, animal.notes, animal.id]
    print(values)
    run_sql(sql, values)
