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

@animals_blueprint.route("/animals/new")
def new_animal():
    vetenarians = vet_repository.select_all()
    return render_template("animals/new.html")

# CREATE new animal

# POST '/animals'

@animals_blueprint.route("/animals/new", methods=['POST'])
def create_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    contact_details = request.form['contact_details']
    notes = request.form['notes']
    vetenarian = vet_repository.select(request.form['vetenarian_id'])
    animal = Animal(name, dob, type, contact_details, vetenarian, notes)
    animal_repository.save(animal)
    return redirect('/animals/success') #--- change this to new SUCCESS page!

# SHOW's new animal submission success

# GET '/animals/<id>'

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/success.html', animal = animal)

# EDIT animal

@animals_blueprint.route("/animals/<id>/edit", methods=['GET'])
def edit_notes(id):
    animal = animal_repository.select(id)
    vetenarians = vet_repository.select_all()
    return render_template('animals/edit.html', animal = animal, all_vetenarians = vetenarians)

# DELETE animal

# FORM with POST method to delete animal.
@animals_blueprint.route("/<id>/delete", methods=['GET'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals/index')