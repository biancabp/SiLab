from flask import Flask, request, render_template, url_for
from flask_login import LoginManager
from flask_migrate import Migrate

from secrets import token_hex
from models.database.database import db
from models.usuario import Usuario
from models.tipo_equipamento import TipoEquipamento

from routes.aula import aula_blueprint
from routes.usuario import usuario_blueprint
from routes.turma import turma_blueprint

from routes.equipamento import equipamento_blueprint
from routes.reagente import reagente_blueprint
from routes.formula_quimica import formula_quimica_blueprint
# from models.formula_quimica import FormulaQuimica
# from models.tipo_equipamento import TipoEquipamento

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
app.register_blueprint(formula_quimica_blueprint)
app.register_blueprint(aula_blueprint)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)