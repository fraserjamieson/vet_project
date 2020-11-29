from flask import Flask, render_template, Blueprint, redirect, request
from models.animals import Animal
from models.vets import Vetenarian
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository


animals_blueprint = Blueprint("animals", __name__) 

# Declare route for list of animals 

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)

# NEW 

# GET

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    vetenarian = vet_repository.select_all()
    return render_template("animals/new.html", all_vetenarians = vetenarian)

# CREATE

# POST '/animals'

@animals_blueprint.route("/animals",  methods=['POST'])
def add_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    contact_details = request.form['contact_details']
    vetenarian = vet_repository.select(vetenarian_id)
    animal = Animal(name, dob, type, contact_details, vetenarian, notes)
    animal_repository.save(animal)
    return redirect('/animals')

# SHOW

# GET '/animals/<id>'

@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/show.html', animal = animal)