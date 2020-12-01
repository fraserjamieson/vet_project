from flask import Flask, render_template, Blueprint, redirect, request
from models.animals import Animal
from models.vets import Vetenarian
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository


animals_blueprint = Blueprint("animals", __name__) 

# INDEX

# GET list of animals

@animals_blueprint.route("/animals", methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    return render_template("/animals/index.html", all_animals = animals)

# NEW

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("/animals/new.html", all_animals = animals, all_vetenarians = vetenarians)

# CREATE 

# REGISTER new animal

@animals_blueprint.route("/animals/new", methods=['POST'])
def create_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    contact_details = request.form["contact_details"]
    notes = request.form["notes"]
    vetenarian = vet_repository.select(request.form["vetenarian_id"])
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian)
    animal_repository.save(animal)
    return redirect("/animals") 

# SHOW 

# list of animals owned by each vet

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    vet_animals = animal_repository.display_vet_animals(id)
    animal = animal_repository.select(id)
    return render_template('/animals/show.html', animal = animal, vetenarian = vet_animals)

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
    animal = Animal(name, dob, animal_type, contact_details, notes, vetenarian, id)
    animal_repository.update(animal)
    return redirect("/animals")

# DELETE

# FORM with POST method to delete animal.

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')