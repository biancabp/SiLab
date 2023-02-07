from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.usuario import Usuario
from models.turma import Turma

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route("/turmas")
@login_required
def turmas():
    if(Usuario.autorizar_professor(current_user) == False):
        return "Usuário não autorizado"

    turmas = Turma.listar()
    return render_template("turmas.html", turmas=turmas)

@turma_blueprint.route('/turmas/cadastrar', methods=['POST'])
@login_required
def cadastrar_turma():
    cod, ano, turno, curso, qtd_alunos = request.form.get('codigo'), int(request.form.get('ano')), request.form.get('turno'), request.form.get('curso'), int(request.form.get('qtd-alunos'))
    Turma(cod, ano, turno, curso, qtd_alunos).cadastrar()

    return render_template('turmas.html')

@turma_blueprint.route('/turmas/editar')
@login_required
def editar_turma():
    id_turma = request.form.get('id-turma')
    cod, ano, turno, curso, qtd_alunos = request.form.get('cod'), request.form.get('ano'), request.form.get('turno'), request.form.get('curso'), request.form.get('qtd_alunos')
    turma = Turma.query.get(id_turma)
    turma.editar(cod, ano, turno, curso, qtd_alunos)

    return render_template('turmas.html')

@turma_blueprint.route('/turmas/deletar')
@login_required
def deletar_turma():
    id_turma = request.form.get('id_turma')
    turma = Turma.query.get(id_turma)
    turma.deletar()

    return render_template('turmas.html')