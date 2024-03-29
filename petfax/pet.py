from flask import (Blueprint, render_template)
import json

pets = json.load(open('./pets.json'))

bp = Blueprint('pet', __name__, url_prefix='/pets')


@bp.route('/')
def index():
    return render_template('/pets/index.html', pets=pets)


@bp.route('/<int:id>')
def show_pet(id):
    return render_template('/pets/show_pet.html', pet=next(filter(lambda p: p['pet_id'] == id, pets)))