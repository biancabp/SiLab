from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.curso import Curso

curso_blueprint = Blueprint('curso', __name__)

@curso_blueprint.route('/cursos')
@login_required
def cursos():
    return render_template('pages/cursos.html')

@curso_blueprint.route('/cursos/cadastrar')
@login_required
def cadastrar_curso():
    novo_curso = Curso(request.form.get('nome-curso'))
    novo_curso.cadastrar()
    return render_template('pages/cursos.html')

@curso_blueprint.route('cursos/editar')
@login_required
def editar_curso():
    id_curso = request.form.get('id-curso')
    curso = Curso.query.get(id_curso)
    curso.edtar(request.form.get('nome-curso'))
    return render_template('pages/cursos.html')

@curso_blueprint.route('cursos/deletar')
@login_required
def deletar_curso():
    id_curso = request.form.get('id-curso')
    curso = Curso.query.get(id_curso)
    curso.deletar()
    return render_template('pages/cursos.html')