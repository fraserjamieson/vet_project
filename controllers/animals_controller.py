from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.vet import Vetenarian
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.customer_repository as customer_repository


animals_blueprint = Blueprint("animals", __name__) 

# INDEX

# GET list of animals

@animals_blueprint.route("/animals", methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/animals/index.html", all_animals = animals, all_customers = customers)

# NEW animal

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    vetenarians = vet_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/animals/new.html", all_vetenarians = vetenarians, all_customers = customers)

# CREATE 

# REGISTER new animal

@animals_blueprint.route("/animals/new", methods=['POST'])
def create_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    contact_details = request.form["contact_details"]
    notes = request.form["notes"]
    customer = customer_repository.select(request.form["customer_id"])
    vetenarian = vet_repository.select(request.form["vetenarian_id"])
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian, customer)
    animal_repository.save(animal)
    return redirect("/animals") 

# EDIT 

@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select(id)
    vetenarians = vet_repository.select_all()
    return render_template('/animals/edit.html', animal = animal, all_vetenarians = vetenarians)

# UPDATE

@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update_animal(id):
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    contact_details = request.form["contact_details"]
    notes = request.form["notes"]
    vetenarian  = vet_repository.select(request.form["vetenarian_id"])
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian,  id)
    animal_repository.update(animal)
    return redirect("/vets")

# DELETE

# FORM with POST method to delete animal.

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')