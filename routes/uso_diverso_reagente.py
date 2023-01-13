from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.uso_diverso_reagente import UsoDiversoReagente

uso_diverso_reagente_blueprint = Blueprint('UsoDiversoReagente', __name__)

@uso_diverso_reagente_blueprint.route('/uso_diverso_reagente')
@login_required
def uso_diverso_reagente():
    return render_template('pages/uso_diverso_reagente.html')

@uso_diverso_reagente_blueprint.route('/uso_diverso_reagente/cadastrar')
@login_required
def cadastrar_uso_diverso_reagente():
    data_uso, massa, descricao, reagente = request.form.get('data-uso'), request.form.get('massa'), request.form.get('descricao'), request.form.get('reagente')
    novo_uso_diverso_reagente = UsoDiversoReagente(data_uso, massa, descricao, reagente)
    novo_uso_diverso_reagente.cadastrar()
    return render_template('pages/uso_diverso_reagente.html')

@uso_diverso_reagente_blueprint.route('/uso_diverso_reagente/editar')
@login_required
def editar_uso_diverso_reagente():
    id_uso_diverso_reagente = request.form.get('id-uso-diverso-reagente')
    data_uso, massa, descricao, reagente = request.form.get('data-uso'), request.form.get('massa'), request.form.get('descricao'), request.form.get('reagente')
    uso_diverso_reagente = UsoDiversoReagente.query.get(id_uso_diverso_reagente)
    uso_diverso_reagente.editar(data_uso, massa, descricao, reagente)
    return render_template('pages/uso_diverso_reagente.html')

@uso_diverso_reagente_blueprint.route('/uso_diverso_reagente/deletar')
@login_required
def deletar_uso_diverso_reagente():
    id_uso_diverso_reagente = request.form.get('id-uso-diverso-reagente')
    uso_diverso_reagente = UsoDiversoReagente.query.get(id_uso_diverso_reagente)
    uso_diverso_reagente.deletar()
    return render_template('pages/uso_diverso_reagente.html')

