from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.equipamento import Equipamento

equipamento_blueprint = Blueprint('equipamento', __name__)

@equipamento_blueprint.route('/equipamentos')
@login_required
def equipamentos():
    return render_template('pages/equipamentos.html')

@equipamento_blueprint.route('/equipamentos/cadastrar')
@login_required
def cadastrar_equipamento():
    localizacao, qtd, volume = request.form.get('localizacao'), request.form.get('qtd'), request.form.get('volume')
    tamanho, tipo_equipamento = request.form.get('tamanho'), request.form.get('tipo-equipamento')
    lugar, danificado = request.form.get('lugar'), request.form.get('danificado')

    novo_equipamento = Equipamento(localizacao, qtd, volume, tamanho, tipo_equipamento, lugar, danificado)
    novo_equipamento.cadastrar()
    return render_template('pages/equipamentos.html')

@equipamento_blueprint.route('/equipamentos/editar')
@login_required
def editar_equipamento():
    id_equipamento = request.form.get('id-equipamento')

    localizacao, qtd, volume = request.form.get('localizacao'), request.form.get('qtd'), request.form.get('volume')
    tamanho, tipo_equipamento = request.form.get('tamanho'), request.form.get('tipo-equipamento')
    lugar, danificado = request.form.get('lugar'), request.form.get('danificado')

    equipamento = Equipamento.query.get(id_equipamento)
    equipamento.editar(localizacao, qtd, volume, tamanho, tipo_equipamento, lugar, danificado)

    return render_template('pages/equipamentos.html')

@equipamento_blueprint.route('/equipamentos/deletar')
@login_required
def deletar_equipamento():
    id_equipamento = request.form.get('id-equipamento')
    equipamento = Equipamento.query.get(id_equipamento)
    equipamento.deletar()

    return render_template('pages/equipamentos.html')