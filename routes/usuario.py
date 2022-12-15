from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user, login_required
from models.usuario import Usuario

usuario_blueprint = Blueprint("usuario", __name__)

@usuario_blueprint.route("/login", methods=["GET", "POST"])
def pagina_login():
    return render_template("login.html")

@usuario_blueprint.route("/autenticar-usuario", methods=["GET", "POST"])
def autenticar_usuario():
    if(request.method == "POST"):
        usuario = Usuario.query.get(int(request.form['matricula']))
        
        if(usuario == None or usuario.senha != request.form['senha']):
            return "Usuário ou senha incorretos"
        
        login_user(usuario)
        return "Usuário Logado!"    
    
    return "método inválido"

@usuario_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return "Usuário deslogado."

@usuario_blueprint.route("/registrar-se")
def registrar_usuario():
    return render_template("cadastro.html")