from flask import Flask, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.customer_repository as customer_repository


animals_blueprint = Blueprint("animals", __name__) 

# INDEX

# GET list of animals at practice

@animals_blueprint.route("/animals", methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("/animals/index.html", all_animals = animals, all_customers = customers)

# NEW animal link to assign

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    customers = customer_repository.select_all()
    return render_template("/animals/new.html", all_customers = customers, title='Animals')

# CREATE 

# actual REGISTER new animal with given link

@animals_blueprint.route("/animals/new", methods=['POST'])
def create_animal():
    print(request.form)
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    notes = request.form["notes"]
    customer = customer_repository.select(request.form["customer_id"])
    animal = Animal(name, dob, animal_type, notes, customer)
    animal_repository.save(animal)
    return redirect("/animals") 

# Link to EDIT chosen existing animal

@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select(id)
    customers = customer_repository.select_all()
    return render_template("/animals/edit.html", title= "Edit Animal", animal = animal, all_customers = customers)

# actual UPDATE of animal entry on link given

@animals_blueprint.route("/animals/<id>/edit", methods=["POST"])
def update_animal(id):
    # takes data from form
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    notes = request.form["notes"]
    customer = customer_repository.select(request.form["customer_id"])

    # make new instance of an Animal using data as constructor values

    animal = Animal(name, dob, animal_type, notes, customer)
    
    # add this new animal object to animal list
    animal_repository.save(animal)
    return redirect("/animals")

# DELETE

# FORM with POST method to delete chosen animal.

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect("/animals")