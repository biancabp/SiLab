from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.professor import Professor
from models.turma import Turma

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route("/turmas")
@login_required
def turmas():
    if(Professor.autorizar_professor(current_user) == False):
        return "Usuário não autorizado"

    turmas = Turma.listar()
    return render_template("turmas.html", turmas=turmas)