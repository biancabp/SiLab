from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user, login_required
from models.usuario import Usuario
from models.formula_quimica import FormulaQuimica

usuario_blueprint = Blueprint("usuario", __name__)

@usuario_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if(len(request.form) == 0):
        return render_template("login.html")

    usuario = Usuario.query.get(int(request.form['matricula']))
    
    if(usuario == None or usuario.senha != request.form['senha']):
        return "Usuário ou senha incorretos"
    
    login_user(usuario)
    formulas_quimica = FormulaQuimica.query.all()
    return render_template('formulas.html', formulas=formulas_quimica)    

@usuario_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return "Usuário deslogado."

@usuario_blueprint.route("/registrar-se", methods=['GET', 'POST'])
def registrar_usuario():
    if len(request.form) == 0:
        return render_template("cadastro.html")

    if request.form['senha'] != request.form['confirme-senha']:
        return "As senhas devem ser iguais."
    
    usuario = Usuario(int(request.form['matricula']), request.form['nome'], request.form['email'], request.form['senha'], request.form['tipo-usuario'])
    usuario.cadastrar()
    return render_template('login.html')