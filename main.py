from flask import Flask, request, render_template
from secrets import token_hex
from models.database.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@host/db_name"
app.config["SECRET_KEY"] = token_hex()

db.init_app(app)

@app.route("/")
def index():
    return "Olá mundo!"