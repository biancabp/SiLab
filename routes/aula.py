from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from models.aula import Aula
from models.usuario import Usuario
from models.turma import Turma
from models.experimento import Experimento

aula_blueprint = Blueprint("aula", __name__, url_prefix='aulas')


@aula_blueprint.route("/", methods=['GET'])
@login_required
def aulas():
    if not Usuario.autorizar_professor(current_user):
        return "Você não tem autorização para acessar esta página."

    aulas = Aula.listar()
    return render_template("aulas.html", aulas=aulas)


@aula_blueprint.route('/cadastrar', methods=['POST'])
@login_required
def cadastrar_aula():
    if not Usuario.autorizar_professor(current_user):
        return "Você não tem autorização para acessar esta página."
    
    nome_aula, turma_cod, data = request.form.get('nome-aula'), request.form.get('turma-cod'), request.form.get('data')
    professor_matricula = request.form.get('professor-matricula')
    planejada_efetivada = request.form.get('planejada-efetivada')
    experimento_id = int(request.form.get('experimento-id'))
    
    Aula(nome_aula, data, planejada_efetivada, Turma.query.get(turma_cod), Usuario.query.get(professor_matricula), Experimento.query.get(experimento_id)).cadastrar()
    redirect(url_for('aulas'))


@aula_blueprint.route('/editar', methods=['PUT'])
@login_required
def editar_aula():
    if not Usuario.autorizar_professor(current_user):
        return "Você não tem autorização para acessar esta página."
    
    id_aula = int(request.form.get('id-aula'))
    aula = Aula.query.get(id_aula)
    
    nome_aula, turma_cod, data = request.form.get('nome-aula'), request.form.get('turma-cod'), request.form.get('data')
    professor_matricula = request.form.get('professor-matricula')
    planejada_efetivada = request.form.get('planejada-efetivada')
    experimento_id = int(request.form.get('experimento-id'))
    
    aula.editar(nome_aula, data, planejada_efetivada, Turma.query.get(turma_cod), Usuario.query.get(professor_matricula), Experimento.query.get(experimento_id))
    redirect(url_for('aulas'))


@aula_blueprint.route('/deletar', methods=['DELETE'])
@login_required
def deletar_aula():
    if not Usuario.autorizar_professor(current_user):
        return "Você não tem autorização para acessar esta página."
    
    id_aula = int(request.form.get('aula-id'))
    aula = Aula.query.get(id_aula)
    aula.deletar()
    redirect(url_for('aulas'))
    