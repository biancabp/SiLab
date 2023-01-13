from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.solucao import Solucao

solucao_blueprint = Blueprint('solucao', __name__)

@solucao_blueprint.route('/solucoees')
@login_required
def solucoes():
    return render_template('pages/solucoes.html')

@solucao_blueprint.route('/solucoes/cadastrar')
@login_required
def cadastrar_solucao():
    nome, autor, formula_quimica = request.form.get('nome'), request.form.get('autor'), request.form.get('formula-quimica')
    estado_materia, densidade, massa = request.form.get('estado-materia'), request.form.get('densidade'), request.form.get('massa')
    concentracao, deletado_planejado = request.form.get('concentracao'), request.form.get('deletado-planejado')
    reagentes = request.form.get('reagentes')

    nova_solucao = Solucao(nome, autor, formula_quimica, estado_materia, densidade, massa, concentracao, deletado_planejado)
    nova_solucao.cadastrar(reagentes)
    return render_template('pages/solucoes.html')

@solucao_blueprint.route('/solucoes/editar')
@login_required
def editar_solucao():
    nome, autor, formula_quimica = request.form.get('nome'), request.form.get('autor'), request.form.get('formula-quimica')
    estado_materia, densidade, massa = request.form.get('estado-materia'), request.form.get('densidade'), request.form.get('massa')
    concentracao, deletado_planejado = request.form.get('concentracao'), request.form.get('deletado-planejado')
    reagentes = request.form.get('reagentes')
    return render_template('pages/solucoes.html')

@solucao_blueprint.route('/solucoes/deletar')
@login_required
def deletar_solucao():
    id_solucao  = request.form.get('id-solucao')
    solucao = Solucao.query.get(id_solucao)
    solucao.deletar()