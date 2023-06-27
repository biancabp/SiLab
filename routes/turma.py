from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.usuario import Usuario
from models.turma import Turma

turma_blueprint = Blueprint("turma", __name__, url_prefix='/turmas')


@turma_blueprint.route("/", methods=['GET'])
@login_required
def turmas():
    if Usuario.autorizar_professor(current_user.matricula) == False:
        return "Usuário não autorizado"

    turmas = Turma.listar()
    return render_template("turmas.html", turmas=turmas)


@turma_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_turma():
    cod, ano, turno, curso, qtd_alunos = request.form.get('codigo'), request.form.get('ano'), request.form.get('turno'), request.form.get('curso'), int(request.form.get('qtd-alunos'))
    Turma(cod, ano, turno, curso, qtd_alunos).cadastrar()
    
    return redirect(url_for('turma.turmas'))


@turma_blueprint.route('/editar', methods=['POST'])
@login_required
def editar_turma():
    cod_original = request.form.get('cod-original')
    novo_cod, ano, turno, curso, qtd_alunos = request.form.get('codigo'), request.form.get('ano'), request.form.get('turno'), request.form.get('curso'), int(request.form.get('qtd-alunos'))
    turma = Turma.query.get({"cod": cod_original})
    turma.editar(novo_cod, ano, turno, curso, qtd_alunos)
    
    return redirect(url_for('turma.turmas'))


@turma_blueprint.route('/deletar', methods=['POST'])
@login_required
def deletar_turma():
    cod_turma = request.form.get('cod-turma')
    turma = Turma.query.get(cod_turma)
    turma.deletar()
    
    return redirect(url_for('turma.turmas'))
