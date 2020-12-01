from flask import Flask, render_template, Blueprint, redirect, request
from models.animals import Animal
from models.vets import Vetenarian
from models.customers import Customers
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("animals", __name__) 