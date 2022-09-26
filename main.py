from flask import Flask, request, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:password@host/db_name"

@app.route("/")
def index():
    return "Olá mundo!"