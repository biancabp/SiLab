from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.aula import Aula
from models.professor import Professor

aula_blueprint = Blueprint("aula", __name__)

@aula_blueprint.route("/aulas")
@login_required
def aulas():
    if(Professor.autorizar_professor(current_user) == False):
        return "Usuário inválido"

    aulas = Aula.listar()
    return render_template("aulas.html", aulas=aulas)