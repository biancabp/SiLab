from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_migrate import Migrate
from models.database.database import db
from models.usuario import Usuario
from secrets import token_hex

from routes.aula import aula_blueprint
from routes.usuario import usuario_blueprint
from routes.turma import turma_blueprint
from routes.equipamento import equipamento_blueprint
from routes.reagente import reagente_blueprint
from routes.formula_quimica import formula_quimica_blueprint
from routes.vidraria import vidraria_blueprint
from routes.uso_diverso_reagente import uso_diverso_reagente_blueprint

# banco

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456789@localhost:3306/silab"
app.config["SECRET_KEY"] = token_hex()

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(reagente_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(turma_blueprint)
app.register_blueprint(equipamento_blueprint)
app.register_blueprint(formula_quimica_blueprint)
app.register_blueprint(aula_blueprint)
app.register_blueprint(vidraria_blueprint)
app.register_blueprint(uso_diverso_reagente_blueprint)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('usuario.login'))


@login_manager.user_loader
def carregar_usuario(matricula):
    return Usuario.query.get(matricula)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
    