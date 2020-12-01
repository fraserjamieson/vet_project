from db.run_sql import run_sql

from models.vet import Vetenarian
from models.animal import Animal 

# create 

def save(vet_to_save):
    sql = "INSERT INTO vetenarians (name) VALUES (%s) RETURNING id"
    values = [vet_to_save.name]
    results = run_sql(sql, values)
    vet_to_save.id = results[0]['id']
    return vet_to_save 

# select

def select(id):
    vetenarian = None
    sql = "SELECT * FROM vetenarians WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vetenarian = Vetenarian(result['name'], result['id'] )
    return vetenarian

# # select all 

def select_all():
    vetenarians = []

    sql = "SELECT * FROM vetenarians"
    results = run_sql(sql)

    for row in results:
        vetenarian = Vetenarian(row['name'], row['id'] )
        vetenarians.append(vetenarian)
    return vetenarians

# # delete

def delete(id):
    sql = "DELETE FROM vetenarian WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# # delete all

def delete_all():
    sql = "DELETE FROM vetenarians"
    run_sql(sql)

# # update (one)

def update(vetenarian):
    sql = "UPDATE vetenarians SET (name) = (%s) WHERE id = %s"
    values = [vetenarian.name, vetenarian.id]
    run_sql(sql, values)

# selects animal with specifically designated vetenarian

def animals(vetenarian):
    animals = []

    sql = "SELECT * FROM animals WHERE vetenarian_id = %s"
    values = [vetenarian.id]
    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['name'], row['DOB'], row['type'], row['contact_details'], row['notes'], row['id'])   #--------REMOVE Vetenarian_ID to fix formatting issue in table
        animals.append(animal)
    return animals