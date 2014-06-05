from flask import Blueprint, render_template


bp = Blueprint('core', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('core/index.html')
