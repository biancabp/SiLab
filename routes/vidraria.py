from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.vidraria import Vidraria

vidraria_blueprint = Blueprint('vidraria', __name__, url_prefix="/vidrarias")


@vidraria_blueprint.route("/", methods=['GET'])
@login_required
def index():
    vidrarias = Vidraria.listar()
    return render_template('vidraria.html', vidrarias=vidrarias)


@vidraria_blueprint.route("/cadastrar", methods=['POST'])
@login_required
def cadastrar_vidraria():
    nome, material, volume = request.form.get('nome'), float(request.form.get('volume')), request.form.get('material')
    local = request.form.get('local')

    Vidraria(volume, material, local).cadastrar()
    redirect(url_for('index'))


@vidraria_blueprint.route("/editar", methods=['PUT'])
@login_required
def editar_vidraria():
    id_vidraria = int(request.form.get('id-vidraria'))
    nome = request.form.get('nome')
    volume = float(request.form.get('volume'))
    material = request.form.get('material')
    local = request.form.get('local')

    vidraria = Vidraria.query.get(id_vidraria)
    vidraria.editar(nome, material, volume, local)

    redirect(url_for('index'))


@vidraria_blueprint.route("/deletar", methods=['DELETE'])
@login_required
def deletar_vidraria():
    id_vidraria = request.form.get('id-vidraria')
    vidraria = Vidraria.query.get(int(id_vidraria))
    vidraria.deletar()

    redirect(url_for('index'))
