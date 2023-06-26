from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.uso_diverso_reagente import UsoDiversoReagente

uso_diverso_reagente_blueprint = Blueprint('UsoDiversoReagente', __name__, url_prefix='uso_diverso_reagente')


@uso_diverso_reagente_blueprint.route('/')
@login_required
def uso_diverso_reagente():
    usos_diversos_reagentes = UsoDiversoReagente.listar()
    return render_template('pages/uso_diverso_reagente.html', usos_diversos_reagentes=usos_diversos_reagentes)


@uso_diverso_reagente_blueprint.route('/cadastrar')
@login_required
def cadastrar_uso_diverso_reagente():
    data_uso, descricao, reagentes = request.form.get('data-uso'), request.form.get('descricao'), request.form.get('reagentes')
    novo_uso_diverso_reagente = UsoDiversoReagente(data_uso, descricao, reagentes)
    novo_uso_diverso_reagente.cadastrar()
    redirect(url_for('uso_diverso_reagente'))


@uso_diverso_reagente_blueprint.route('/editar')
@login_required
def editar_uso_diverso_reagente():
    id_uso_diverso_reagente = int(request.form.get('id-uso-diverso-reagente'))
    data_uso, descricao, reagentes = request.form.get('data-uso'), request.form.get('descricao'), request.form.get('reagentes')
    uso_diverso_reagente = UsoDiversoReagente.query.get(id_uso_diverso_reagente)
    uso_diverso_reagente.editar(data_uso, descricao, reagentes)
    redirect(url_for('uso_diverso_reagente'))


@uso_diverso_reagente_blueprint.route('/deletar')
@login_required
def deletar_uso_diverso_reagente():
    id_uso_diverso_reagente = int(request.form.get('id-uso-diverso-reagente'))
    uso_diverso_reagente = UsoDiversoReagente.query.get(id_uso_diverso_reagente)
    uso_diverso_reagente.deletar()
    redirect(url_for('uso_diverso_reagente'))
