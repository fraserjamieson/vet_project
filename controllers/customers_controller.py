from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vetenarian_repository as vetenarian_repository
import repositories.customer_repository as customer_repository


customers_blueprint = Blueprint("customers", __name__) 

# INDEX

# GET list of customers

@customers_blueprint.route("/customers", methods=['GET'])
def customers():
    customers = customer_repository.select_all()
    return render_template("/customers/index.html", all_animals = animals, all_customers = customers)

# NEW customer

@customers_blueprint.route("/customers/new", methods=['GET'])
def new_customer():
    vetenarians = vetenarian_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/customers/new.html", all_vetenarians = vetenarians, all_customers = customers)

# CREATE 

# REGISTER new customer

@customers_blueprint.route("/customers/new", methods=['POST'])
def create_customer():
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    customer = customer_repository.select(request.form["customer_id"])
    vetenarian = vetenarian_repository.select(request.form["vetenarian_id"])
    customer = Customer(name, contact_details, vetenarian)
    customer_repository.save(customer)
    return redirect("/customers") 

# EDIT 

@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    animals = animal_repository.select.all()
    vetenarians = vetenarian_repository.select_all()
    return render_template("/customers/edit.html", title= "Edit Customer", customer - customer, all_vetenarians = vetenarians, all_animals = animals)

# UPDATE

@customers_blueprint.route("/customers/<id>/edit", methods=["POST"])
def update_customer(id):
    # takes data from form
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    vetenarian  = vetenarian_repository.select(request.form["vetenarian_id"])

    # make new instance of a Customer using data as constructor values

    customer = Customer(name, contact_details, vetenarian)
    
    # add this new customer object to customer list
    customer_repository.save(customer)
    return redirect("/customers")

# DELETE

# FORM with POST method to delete customer.

@customers_blueprint.route("/customers/<id>/delete", methods=['POST'])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")