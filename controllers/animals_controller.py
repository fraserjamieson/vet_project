from flask import Flask, render_template, Blueprint
from models.animals import Animal


animals_blueprint = Blueprint("animals", __name__) 

# Index for home page

# Declare route for list of animals 
@animals_blueprint.route("/animals")
def animals():
    return render_template("animals/index.html")