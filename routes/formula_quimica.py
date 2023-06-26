from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.formula_quimica import FormulaQuimica

formula_quimica_blueprint = Blueprint('formula_quimica', __name__, url_prefix='formula_quimica')


@formula_quimica_blueprint.route('/', methods=['GET'])
@login_required
def formulas_quimica():
    formulas = FormulaQuimica.query.all()
    return render_template('formulas.html', formulas=formulas)


@formula_quimica_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_formula_quimica():
    formula_quimica, nome = request.form.get('formula-quimica'), request.form.get('nome')
    FormulaQuimica(formula_quimica, nome).cadastrar()
    redirect(url_for('formulas_quimica'))


@formula_quimica_blueprint.route('/editar', methods=['PUT'])
@login_required
def editar_formula_quimica():
    formula_original = request.form.get('formula-quimica')
    formula_quimica = FormulaQuimica.query.get(formula_original)

    nova_formula = request.form.get('nova-formula-quimica')
    novo_nome = request.form.get('nome')
    formula_quimica.editar(nova_formula, novo_nome)
    
    redirect(url_for('formulas_quimica'))


@formula_quimica_blueprint.route('/deletar', methods=['DELETE'])
@login_required
def deletar_formula_quimica():
    formula_quimica = request.form.get('formula-quimica')
    formula_quimica = FormulaQuimica.query.get(formula_quimica)
    formula_quimica.deletar()
    redirect(url_for('formulas_quimica'))
