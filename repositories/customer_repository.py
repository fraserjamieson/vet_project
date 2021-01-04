from db.run_sql import run_sql
from models.customer import Customer
from models.vetenarian import Vetenarian
from models.animal import Animal
import repositories.vetenarian_repository as vetenarian_repository

def save(customer):
    sql = "INSERT INTO customers (name, contact_details, vet_id) VALUES (%s, %s, %s) RETURNING *"
    values = [customer.name, customer.contact_details, customer.vet.id]
    results = run_sql(sql, values)
    customer.id = results[0]['id']
    return customer
    
def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    for row in results:
        vetenarian = vetenarian_repository.select(row['vetenarian_id'])
        customer = Customer(row["name"], vet, row["animals"], row["id"])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql ="SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
   
    if result is not None:
        vetenarian = vetenarian_repository.select(result['vetenarian_id'])
        customer = Customer(result['name'], vetenarian,  result['id'])
    return customer 

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    vaules = [id]
    run_sql(sql, vaules)

def update(customer):
    sql = "UPDATE customers SET (name) = (%s) WHERE id = %s"
    values = [customer.name, customer.contact_details, customer.id]
    run_sql(sql, values)