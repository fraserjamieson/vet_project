from flask import flash, render_template, Blueprint, redirect, request
from models.animal import Animal
from models.customer import Customer
import repositories.animal_repository as animal_repository
import repositories.customer_repository as customer_repository


customers_blueprint = Blueprint("customers", __name__) 

# INDEX

# GET list of customers and their animals

@customers_blueprint.route("/customers", methods=['GET'])
def customers():
    customers = customer_repository.select_all()
    # customers_animals = customer_repository.display_customer_animals(id)
    animals = animal_repository.select_all()
    return render_template("/customers/index.html", all_animals = animals, all_customers = customers)


# CREATE 

# NEW customer

@customers_blueprint.route("/customers/new", methods=['GET'])
def new_customer():
    customers = customer_repository.select_all()
    return render_template("/customers/new.html", all_customers = customers, title='Customers')

# REGISTER new customer

@customers_blueprint.route("/customers/new", methods=['POST'])
def create_customer():

    name = request.form["name"]
    contact_details = request.form["contact_details"]
    # customer = customer_repository.select(request.form["customer_id"])
    newCustomer = Customer(name, contact_details)
    customer_repository.save(newCustomer)

    flash("New customer registered!")

    return redirect("/customers") 

# EDIT 

@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    animals = animal_repository.select_all()
    return render_template("/customers/edit.html", title= "Edit Customer", customer = customer, all_animals = animals)

# UPDATE

@customers_blueprint.route("/customers/<id>/edit", methods=["POST"])
def update_customer(id):
    # takes data from form
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    # make new instance of a Customer using data as constructor values
    customer = Customer(name, contact_details)
    # add this new customer object to customer list
    customer_repository.save(customer)
    return redirect("/customers")

# DELETE

# FORM with POST method to delete customer.

@customers_blueprint.route("/customers/<id>/delete", methods=['POST'])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")