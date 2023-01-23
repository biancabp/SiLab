from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.tipo_equipamento import TipoEquipamento

tipo_equipamento_blueprint = Blueprint('tipo_equipamento', __name__)

@tipo_equipamento_blueprint.route('/tipo_equipamento')
@login_required
def tipo_equipamento():
    return render_template('pages/tipo_equipamento.html')

@tipo_equipamento_blueprint.route('/tipo_equipamento/cadastrar')
@login_required
def cadastrar_tipo_equipamento():
    nome = request.form.get('nome')
    TipoEquipamento(nome).cadastrar()
    return render_template('pages/tipo_equipamento.html')

@tipo_equipamento_blueprint.route('/tipo_equipamento/editar')
@login_required
def editar_tipo_equipamento():
    id_tipo_equipamento = request.form.get('id-tipo-equipamento')
    novo_nome = request.form.get('novo-nome')

    tipo_equipamento = TipoEquipamento.query.get(id_tipo_equipamento)
    tipo_equipamento.editar(novo_nome)
    return render_template('pages/tipo_equipamento.html')

@tipo_equipamento_blueprint.route('/tipo_equipamento/deletar')
@login_required
def deletar_tipo_equipamento():
    id_tipo_equipamento = request.form.get('id-tipo-equipamento')
    tipo_equipamento = TipoEquipamento.query.get(id_tipo_equipamento)
    tipo_equipamento.deletar()
    return render_template('pages/tipo_equipamento.html')