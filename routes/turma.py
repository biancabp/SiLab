from flask import Blueprint, render_template

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route("/turma")
def turma():
    return render_template("turmas.html")