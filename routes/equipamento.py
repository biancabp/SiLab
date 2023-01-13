from flask import Blueprint, render_template
from flask_login import login_required, current_user

equipamento_blueprint = Blueprint('equipamento', __name__)

@equipamento_blueprint.route('/equipamentos')
@login_required
def equipamentos():
    return render_template('pages/equipamentos.html')