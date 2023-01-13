from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.reagente import Reagente

reagente_blueprint = Blueprint('reagente', __name__)

@reagente_blueprint.route('/reagentes')
@login_required
def reagentes():
    return render_template('pages/reagentes.html')

@reagente_blueprint.route('/reagentes/cadastrar')
@login_required
def cadastrar_reagente():
    nome, estado_materia, densidade = request.form.get('nome'), request.form.get('estado_materia'), request.form.get('densidade')
    massa, volume, data_validade = request.form.get('massa'), request.form.get('volume'), request.form.get('data-validade')
    formula_quimica = request.form.get('formula-quimica')
    novo_reagente = Reagente(nome, estado_materia, densidade, massa, volume, data_validade, formula_quimica, False)
    novo_reagente.cadastrar()

    return render_template('pages/reagentes.html')

@reagente_blueprint.route('/reagentes/editar')
@login_required
def editar_reagente():
    id_reagente = request.form.get('id-reagente')
    nome, estado_materia, densidade = request.form.get('nome'), request.form.get('estado_materia'), request.form.get('densidade')
    massa, volume, data_validade = request.form.get('massa'), request.form.get('volume'), request.form.get('data-validade')
    formula_quimica = request.form.get('formula-quimica')

    reagente = Reagente.query.get(id_reagente)
    reagente.editar(nome, estado_materia, densidade, massa, volume, data_validade, formula_quimica)
    return render_template('pages/reagentes.html')

@reagente_blueprint.route('/reagentes/deletar')
@login_required
def deletar_reagente():
    id_reagente = request.form.get('id-reagente')
    reagente = Reagente.query.form.get(id_reagente)
    reagente.deletar()
    return render_template('pages/reagentes.html')