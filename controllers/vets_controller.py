from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.customer_repository as customer_repository

vets_blueprint = Blueprint("vets", __name__) 

# INDEX 
# 
# list of vets

# This show animals cared for, but has bug.  need to show animals cared for by SPECIFIC vet

@vets_blueprint.route("/vets", methods=['GET'])
def vets():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('/vets/index.html', all_vetenarians = vetenarians, all_customers = customers, all_animals = animals)

# SHOW customers

# @vets_blueprint.route("/vets/customer", methods=['GET'])
# def customers(id):
#     animals = animal_repository.select(id)
#     customer = customer_repository.select(id)
#     customer_animals = animal_repository.display_vet_animals(id)
#     return render_template('/vets/customer.html', animals = animals, customer_animals = customer_animals, customer = customer)

# @vets_blueprint.route("/vets/customer", methods=['GET'])
# def vets():  
#     customers = customer_repository.select_all()
#     return render_template("/vets/customer.html", all_customers = customers)

# DELETE

# FORM with POST method to delete animal.

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/vets')

# NEW customer

# Get customer info

@vets_blueprint.route("/vets/new", methods=['GET'])
def new_customer():
    vetenarians = vet_repository.select_all()
    return render_template('/vets/new.html', )

# CREATE 

# REGISTER new customer

@vets_blueprint.route("/vets/new", methods=['POST'])
def create_customer():
    name = request.form["name"]
    vetenarian = vet_repository.select(request.form["vetenarian_id"])

    customer = Customer(name, vetenarian)
    vet_repository.save(customer)
    return redirect("/vets") 