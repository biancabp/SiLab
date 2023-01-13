from flask import Blueprint, render_template
from flask_login import login_required, current_user

reagente_blueprint = Blueprint('reagente', __name__)

@reagente_blueprint.route('/reagentes')
@login_required
def reagentes():
    return render_template('pages/reagentes.html')