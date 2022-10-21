from flask import Blueprint, render_template

usuario_blueprint = Blueprint("usuario", __name__,)

@usuario_blueprint.route("/login", methods=["GET", "POST"])
def pagina_login():
    return render_template("login.html")