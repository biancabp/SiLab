from flask import Flask, request, render_template, url_for
from flask_login import LoginManager

from secrets import token_hex
from models.database.database import db

from routes.aula import aula_blueprint
from routes.usuario import usuario_blueprint
from routes.turma import turma_blueprint
from models.usuario import Usuario
from models.curso import Curso
from flask_migrate import Migrate
from routes.equipamento import equipamento_blueprint
from routes.reagente import reagente_blueprint
from models.formula_quimica import FormulaQuimica

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SECRET_KEY"] = token_hex()

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def carregar_usuario(matricula):
    return Usuario.query.get(matricula)

app.register_blueprint(reagente_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(turma_blueprint)
app.register_blueprint(equipamento_blueprint)
app.run("0.0.0.0", debug=True)