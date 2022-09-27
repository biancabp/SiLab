from flask import Flask, request, render_template
from secrets import token_hex

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@host/db_name"
app.config["SECRET_KEY"] = token_hex()

@app.route("/")
def index():
    return "Olá mundo!"