from db.run_sql import run_sql
from models.customers import Customer
from models.vets import Vetenarian
from models.animal import Animal

def save(customer):
    sql = "INSERT INTO customers (name) VALUES (%s) RETURNING id"
    values = [customer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id

def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for result in results:
        customers = Customer(
            result["name"], 
            result["id"])
        customers.append(customer)
    return customers

def select(id):
    sql ="SELECT * FROM customers where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
   
    if result is not None:
     customer = Customer(
        result["name"], 
        result["id"])
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
    values = [customer.name, customer.id]
    run_sql(sql, values)