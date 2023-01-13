from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.aula import Aula
from models.usuario import Usuario

aula_blueprint = Blueprint("aula", __name__)

@aula_blueprint.route("/aulas")
@login_required
def aulas():
    if(Usuario.autorizar_professor(current_user) == False):
        return "Usuário inválido"

    aulas = Aula.listar()
    return render_template("aulas.html", aulas=aulas)

@aula_blueprint.route('/aulas/cadastrar')
@login_required
def cadastrar_aula():
    turma, data, roteiro = request.form.get('turma'), request.form.get('data'), request.form.get('roteiro')
    professor, planejada_efetivada, equipamentos = request.form.get('professor'), request.form.get('planejada-efetivada'), request.form.get('equipamentos')
    reagentes, solucoes_criadas = request.form.get('reagentes'), request.form.get('solucoes-criadas')
    solucoes_utilizadas, solucoes_criadas_utilizadas = request.form.get('solucoes-utilizadas'), request.form.get('solucoes-criadas-utilizadas')
    
    nova_aula = Aula(turma, data, roteiro, professor, planejada_efetivada)
    nova_aula.cadastrar_aula(equipamentos, reagentes, solucoes_criadas, solucoes_utilizadas, solucoes_criadas_utilizadas)
    return render_template('pages/aulas.html')

@aula_blueprint.route('/aulas/editar')
@login_required
def editar_aula():
    id_aula = request.form.get('id-aula')

    turma, data, roteiro = request.form.get('turma'), request.form.get('data'), request.form.get('roteiro')
    professor, planejada_efetivada, equipamentos = request.form.get('professor'), request.form.get('planejada-efetivada'), request.form.get('equipamentos')
    reagentes, solucoes_criadas = request.form.get('reagentes'), request.form.get('solucoes-criadas')
    solucoes_utilizadas, solucoes_criadas_utilizadas = request.form.get('solucoes-utilizadas'), request.form.get('solucoes-criadas-utilizadas')

    aula = Aula.query.get(id_aula)
    aula.editar()

@aula_blueprint.route('/aulas/deletar')
@login_required
def deletar_aula():
    id_aula = request.form.get('id-aula')
    aula = Aula.query.get(id_aula)
    aula.deletar()
    return render_template('pages/aulas.html')