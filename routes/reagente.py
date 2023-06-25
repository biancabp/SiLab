from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.reagente import Reagente
from models.formula_quimica import FormulaQuimica

reagente_blueprint = Blueprint('reagente', __name__)


@reagente_blueprint.route('/reagentes')
@login_required
def reagentes():
    reagentes = Reagente.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('reagentes.html', reagentes=reagentes, formulas_quimica=formulas_quimica, round=round)


@reagente_blueprint.route('/reagentes/cadastrar', methods=['POST'])
@login_required
def cadastrar_reagente():
    estado_materia, densidade = request.form.get('estado-materia'), request.form.get('densidade')
    massa, volume, data_validade = request.form.get('massa'), request.form.get('volume'), request.form.get('data-validade')
    formula_quimica, local = request.form.get('formula-quimica'), request.form.get('local')
    novo_reagente = Reagente(estado_materia, densidade, massa, volume, data_validade, formula_quimica, False)
    novo_reagente.cadastrar()

    reagentes = Reagente.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('reagentes.html', reagentes=reagentes, formulas_quimica=formulas_quimica, round=round)


@reagente_blueprint.route('/reagentes/editar', methods=['POST'])
@login_required
def editar_reagente():
    id_reagente = request.form.get('id-reagente')

    estado_materia, densidade = request.form.get('estado-materia'), request.form.get('densidade')
    massa, volume, data_validade = request.form.get('massa'), request.form.get('volume'), request.form.get('data-validade')
    formula_quimica, local = request.form.get('formula-quimica'), request.form.get('local')

    reagente = Reagente.query.get(id_reagente)
    reagente.editar(estado_materia, densidade, massa, volume, data_validade, formula_quimica, local)
   
    reagentes = Reagente.query.all()
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('reagentes.html', reagentes=reagentes, formulas_quimica=formulas_quimica, round=round)


@reagente_blueprint.route('/reagentes/deletar')
@login_required
def deletar_reagente():
    id_reagente = request.form.get('id-reagente')
    reagente = Reagente.query.form.get(id_reagente)
    reagente.deletar()
    return render_template('reagentes.html')