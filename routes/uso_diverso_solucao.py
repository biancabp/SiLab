from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.uso_diverso_solucao import UsoDiversoSolucao

uso_diverso_solucao_blueprint = Blueprint('UsoDiversoSolucao', __name__)

@uso_diverso_solucao_blueprint.route('/uso_diverso_solucao')
@login_required
def uso_diverso_solucao():
    return render_template('pages/uso_diverso_solucao.html')

@uso_diverso_solucao_blueprint.route('/uso_diverso_solucao/cadastrar')
@login_required
def cadastrar_uso_diverso_solucao():
    data_uso, massa, descricao, solucao = request.form.get('data-uso'), request.form.get('massa'), request.form.get('descricao'), request.form.get('solucao')
    novo_uso_diverso_solucao = UsoDiversoSolucao(data_uso, massa, descricao, solucao)
    novo_uso_diverso_solucao.cadastrar()
    return render_template('pages/uso_diverso_solucao.html')

@uso_diverso_solucao_blueprint.route('/uso_diverso_solucao/editar')
@login_required
def editar_uso_diverso_solucao():
    id_uso_diverso_solucao = request.form.get('id-uso-diverso-solucao')
    data_uso, massa, descricao, solucao = request.form.get('data-uso'), request.form.get('massa'), request.form.get('descricao'), request.form.get('solucao')
    uso_diverso_solucao = UsoDiversoSolucao.query.get(id_uso_diverso_solucao)
    uso_diverso_solucao.editar(data_uso, massa, descricao, solucao)
    return render_template('pages/uso_diverso_solucao.html')

@uso_diverso_solucao_blueprint.route('/uso_diverso_solucao/deletar')
@login_required
def deletar_uso_diverso_solucao():
    id_uso_diverso_solucao = request.form.get('id-uso-diverso-solucao')
    uso_diverso_solucao = UsoDiversoSolucao.query.get(id_uso_diverso_solucao)
    uso_diverso_solucao.deletar()
    return render_template('pages/uso_diverso_solucao.html')

