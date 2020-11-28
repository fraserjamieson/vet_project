from db.run_sql import run_sql

from models.vets import Vetenarian

# create 
def save(vet_to_save):
    sql = "INSERT INTO vetenarians (name) VALUES (%s) RETURNING id"
    values = [vet_to_save.name]
    results = run_sql(sql, values)
    vet_to_save.id = results[0]['id']
    return vet_to_save 

# read one

# read all

# select

# # select all 

# # delete

# # delete all

# # update (one)
