from flask import Blueprint, render_template
from models.aula import Aula

aula_blueprint = Blueprint("aula", __name__)

@aula_blueprint.route("/aula")
def aulas():
    aulas = Aula.listar(None, None)
    return render_template("aulas.html", aulas=aulas)