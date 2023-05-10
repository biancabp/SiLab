from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.vidraria import Vidraria

vidraria_blueprint = Blueprint('vidraria', __name__, url_prefix = "vidraria")

@vidraria_blueprint.route("/")
def index():
    return render_template('vidraria.html')

@vidraria_blueprint.route("/cadastrar")
def cadastrar_vidraria():
    volume = request.form.get('volume')
    material = request.form.get('material')
    local = request.form.get('local')

    Vidraria(volume, material, local).cadastrar()

    vidrarias = Vidraria.listar()
    return render_template('vidraria.html', vidrarias=vidrarias)

@vidraria_blueprint.route("/editar")
def editar_vidraria():
    id_vidraria = request.form.get('id-vidraria')
    volume = request.form.get('volume')
    material = request.form.get('material')
    local = request.form.get('local')

    vidraria = Vidraria.query.get(int(id_vidraria))
    vidraria.editar(volume, material, local)

    vidrarias = Vidraria.listar()
    return render_template('vidraria.html', vidrarias=vidrarias)

@vidraria_blueprint.route("/deletar")
def deletar_vidraria():
    id_vidraria = request.form.get('id-vidraria')
    vidraria = Vidraria.query.get(int(id_vidraria))
    vidraria.deletar()

    vidrarias = Vidraria.listar()

    return render_template('vidrarias.html', vidrarias=vidrarias)