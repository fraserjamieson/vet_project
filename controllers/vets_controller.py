from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.customer_repository as customer_repository

vets_blueprint = Blueprint("vets", __name__) 

# INDEX

# GET list of vets, animals and customers

@vets_blueprint.route("/vets", methods=['GET'])
def vets():  
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/vets/index.html", all_vetenarians = vetenarians, all_animals = animals, all_customers = customers)

# NEW animal

@vets_blueprint.route("/vets/newanimal", methods=['GET'])
def new_animal():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("/animals/new.html", all_animals = animals, all_vetenarians = vetenarians, all_customers = customers)

# CREATE 

# REGISTER new animal

@vets_blueprint.route("/vets/newanimal", methods=['POST'])
def create_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    contact_details = request.form["contact_details"]
    notes = request.form["notes"]
    vetenarian = vet_repository.select(request.form["vetenarian_id"])
    customer = customer_repository.select(request.form["customer_id"])
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian, customer)
    animal_repository.save(animal)
    return redirect("/vets") 

# SHOW 

# animals owned by each vet

@vets_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    vet_animals = animal_repository.display_vet_animals(id)
    return render_template('/animals/show.html', animal = animal, vetenarian = vet_animals)

# EDIT 

@vets_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select(id)
    vetenarians = vet_repository.select_all()
    return render_template('/animals/edit.html', animal = animal, all_vetenarians = vetenarians)

# UPDATE

@vets_blueprint.route("/animals/<id>", methods=["POST"])
def update_animal(id):
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    contact_details = request.form["contact_details"]
    notes = request.form["notes"]
    vetenarian  = vet_repository.select(request.form["vetenarian_id"])
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian, id)
    animal_repository.update(animal)
    return redirect("/animals")

# DELETE

# FORM with POST method to delete animal.

@vets_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')