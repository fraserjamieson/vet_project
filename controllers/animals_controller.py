from flask import Flask, render_template, Blueprint, redirect, request
from models.animals import Animal
from models.vets import Vetenarian
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository


animals_blueprint = Blueprint("animals", __name__) 

# GET list of animals

@animals_blueprint.route("/animals", methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)

# NEW

@animals_blueprint.route("/animals/new")
def new_animal():
    vetenarians = vet_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("animals/new.html", all_animals = animals, all_vetenarians = vetenarians)

# CREATE 

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

# SHOW's new animal submission success

# GET '/animals/<id>'

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/success.html', animal = animal)

# EDIT 

@animals_blueprint.route("/animals/<id>/edit", methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/edit.html', animal = animal)

# DELETE

# FORM with POST method to delete animal.
@animals_blueprint.route("/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals/')