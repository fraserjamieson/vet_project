from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vetenarian_repository as vetenarian_repository
import repositories.customer_repository as customer_repository

vetenarians_blueprint = Blueprint("vetenerians", __name__) 

# INDEX 

# Declare a route for the list of vets

@vets_blueprint.route("/vetenarians", methods=['GET'])
def vets():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('/vetenarians/index.html', all_vetenarians = vetenarians, all_customers = customers, all_animals = animals)

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

# ------------

# NEW customer

# # Get customer info

# @vets_blueprint.route("/vets/get", methods=['GET'])
# def get_customer():
#     vetenarians = vet_repository.select_all()
#     return render_template('/vets/new.html', )

# # CREATE 

# # REGISTER new customer

# @vets_blueprint.route("/vets/new", methods=['POST'])
# def create_customer():
#     name = request.form["name"]
#     vetenarian = vet_repository.select(request.form["vetenarian_id"])
#     customer = Customer(name, contact_details, vetenarian)
#     vet_repository.save(customer)
#     return redirect("/vets") 