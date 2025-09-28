from flask import Blueprint, render_template

duvidas_bp = Blueprint('duvidas_bp', __name__, template_folder='templates')

@duvidas_bp.route('/duvidas')
def duvidas():
    return render_template('duvida.html')
