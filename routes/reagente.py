from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.reagente import Reagente
from models.formula_quimica import FormulaQuimica

reagente_blueprint = Blueprint('reagente', __name__, url_prefix='/reagentes')


@reagente_blueprint.route('/', methods=['GET'])
@login_required
def reagentes():
    reagentes = Reagente.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('reagentes.html', reagentes=reagentes, formulas_quimica=formulas_quimica, round=round)


@reagente_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_reagente():
    estado_materia, concentracao = request.form.get('estado-materia'), float(request.form.get('concentracao'))
    massa, volume, data_validade = float(request.form.get('massa')), float(request.form.get('volume')), request.form.get('data-validade')
    formula_quimica, local, data_criacao = request.form.get('formula-quimica'), request.form.get('local'), request.form.get('data-criacao')
    novo_reagente = Reagente(estado_materia, concentracao, massa, volume, formula_quimica, local, data_validade, data_criacao)
    novo_reagente.cadastrar()

    redirect(url_for('reagentes'))


@reagente_blueprint.route('/editar', methods=['PUT'])
@login_required
def editar_reagente():
    id_reagente = int(request.form.get('id-reagente'))

    estado_materia, concentracao = request.form.get('estado-materia'), request.form.get('concentracao')
    massa, volume, data_validade = request.form.get('massa'), request.form.get('volume'), request.form.get('data-validade')
    formula_quimica, local, data_criacao = request.form.get('formula-quimica'), request.form.get('local'), request.form.get('data-criacao')

    reagente = Reagente.query.get(id_reagente)
    reagente.editar(estado_materia, concentracao, massa, volume, data_validade, formula_quimica, local)
   
    redirect(url_for('reagentes'))


@reagente_blueprint.route('/deletar', methods=['DELETE'])
@login_required
def deletar_reagente():
    id_reagente = int(request.form.get('id-reagente'))
    reagente = Reagente.query.form.get(id_reagente)
    reagente.deletar()
    redirect(url_for('reagentes'))
