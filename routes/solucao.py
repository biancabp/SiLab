from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.solucao import Solucao
from models.formula_quimica import FormulaQuimica

solucao_blueprint = Blueprint('solucao', __name__)

@solucao_blueprint.route('/solucoes')
@login_required
def solucoes():
    solucoes = Solucao.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('solucoes.html', solucoes=solucoes, formulas_quimica=formulas_quimica, round=round)

@solucao_blueprint.route('/solucoes/cadastrar', methods=['POST'])
@login_required
def cadastrar_solucao():
    formula_quimica, local = request.form.get('formula-quimica'), request.form.get('local')
    estado_materia, densidade, massa = request.form.get('estado-materia'), request.form.get('densidade'), request.form.get('massa')
    concentracao, deletado_planejado = request.form.get('concentracao'), request.form.get('deletado-planejado')
    reagentes, data_validade, volume = request.form.get('reagentes'), request.form.get('data-validade'), request.form.get('volume')

    nova_solucao = Solucao(formula_quimica, estado_materia, densidade, massa, concentracao, local, data_validade, volume, deletado_planejado)
    nova_solucao.cadastrar(reagentes)

    solucoes = Solucao.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('solucoes.html', solucoes=solucoes, formulas_quimica=formulas_quimica, round=round)

@solucao_blueprint.route('/solucoes/editar', methods=['POST'])
@login_required
def editar_solucao():
    id_solucao = request.form.get('id-solucao')

    formula_quimica = request.form.get('formula-quimica')
    estado_materia, densidade, massa = request.form.get('estado-materia'), request.form.get('densidade'), request.form.get('massa')
    concentracao, volume, data_validade, local = request.form.get('concentracao'), request.form.get('volume'), request.form.get('data-validade'), request.form.get('local')
    
    # reagentes = request.form.get('reagentes')
    
    solucao = Solucao.query.get(id_solucao)
    solucao.editar(formula_quimica, estado_materia, massa, densidade, concentracao, volume, data_validade, local)
    
    solucoes = Solucao.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('solucoes.html', solucoes=solucoes, formulas_quimica=formulas_quimica, round=round)

@solucao_blueprint.route('/solucoes/deletar')
@login_required
def deletar_solucao():
    id_solucao  = request.form.get('id-solucao')
    solucao = Solucao.query.get(id_solucao)
    solucao.deletar()