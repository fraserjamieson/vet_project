from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.customer_repository as customer_repository

vets_blueprint = Blueprint("vets", __name__) 

# INDEX

# @vets_blueprint.route("/vets", methods=['GET'])
# def vets():  
#     vetenarians = vet_repository.select_all()
#     vet_animals = vet_repository.vet_animals()
#     animals = animal_repository.select_all()
#     customers = customer_repository.select_all()
#     return render_template("/vets/index.html", all_vetenarians = vetenarians, all_animals = animals, all_customers = customers, all_vets_animals = vets_animals)

# SHOW 

@vets_blueprint.route("/vets", methods=['GET'])
def show_vets_animals():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('/vets/index.html', all_vetenarians = vetenarians, all_customers = customers, all_animals = animals)

# DELETE

# FORM with POST method to delete animal.

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/vets')