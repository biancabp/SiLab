from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.equipamento import Equipamento

equipamento_blueprint = Blueprint('equipamento', __name__, url_prefix='/equipamentos')


@equipamento_blueprint.route('/', methods=['GET'])
@login_required
def equipamentos():
    equipamentos = Equipamento.listar()
    return render_template('equipamentos.html', equipamentos=equipamentos)


@equipamento_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_equipamento():
    tombo, tipo_equipamento = request.form.get('tombo'), request.form.get('tiipo-equipamento')
    descricao, local = request.form.get('descricao'), request.form.get('local')

    novo_equipamento = Equipamento(tombo, tipo_equipamento, descricao, local)
    novo_equipamento.cadastrar()
    redirect(url_for('equipamentos'))


@equipamento_blueprint.route('/editar', methods=['PUT'])
@login_required
def editar_equipamento():
    tombo_original = request.form.get('tombo-original')

    novo_tombo, tipo_equipamento = request.form.get('novo-tombo'), request.form.get('tiipo-equipamento')
    descricao, local = request.form.get('descricao'), request.form.get('local')

    equipamento = Equipamento.query.get(tombo_original)
    equipamento.editar(novo_tombo, tipo_equipamento, descricao, local)

    redirect(url_for('equipamentos'))


@equipamento_blueprint.route('/deletar', methods=['DELETE'])
@login_required
def deletar_equipamento():
    tombo_equipamento = request.form.get('tombo-equipamento')
    equipamento = Equipamento.query.get(tombo_equipamento)
    equipamento.deletar()

    redirect(url_for('equipamento'))
