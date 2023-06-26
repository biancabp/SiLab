from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.experimento import Experimento

experimento_blueprint = Blueprint('experimento', __name__, url_prefix='/experimentos')


@experimento_blueprint.route('/', methods=['GET'])
@login_required
def experimentos():
    experimentos = Experimento.query.filter(Experimento.ideal_concreto == 'ideal').all()
    return render_template('experimentos.html', experimentos=experimentos)


@experimento_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_experimento():
    nome, arquivo = request.form.get('nome'), request.files.get('arquivo')
    vidrarias, equipamentos = request.form.get('vidrarias'), request.form.get('equipamentos')
    reagentes, reagentes_planejados = request.form.get('reagentes'), request.form.get('reagentes-planejados')
    
    Experimento(nome, arquivo, equipamentos, vidrarias, reagentes, reagentes_planejados).cadastrar()
    redirect(url_for('experimentos'))
    

@experimento_blueprint.route('/editar', methods=['PUT'])
@login_required
def editar_experimento():
    experimento_id = int(request.form.get('experimento-id'))
    experimento = Experimento.query.get(experimento_id)
    
    nome, arquivo, equipamentos = request.form.get('nome'), request.files.get('arquivo'), request.form.get('equipamentos')
    vidrarias, reagentes, reagentes_planejados = request.form.get('vidrarias'), request.form.get('reagentes'), request.form.get('reagentes-planejados')
    
    experimento.editar(nome, arquivo, equipamentos, vidrarias, reagentes, reagentes_planejados)
    redirect(url_for('experimentos'))
    

@experimento_blueprint.route('/deletar', methods=['DELETE'])
@login_required
def deletar_experimento():
    experimento_id = int(request.form.get('equipamento-id'))
    experimento = Experimento.query.get(experimento_id)
    experimento.deletar()
    redirect(url_for('experimentos'))
    