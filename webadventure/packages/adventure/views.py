from flask import Blueprint, render_template
from .forms import PromptField
from webadventure.app import app

bp = Blueprint('prompt', __name__, url_prefix='/user')

@bp.route('/prompt/', methods=['GET', 'POST'])
def prompt_view():
    form = PromptField()
    return render_template('user/prompt.html',
                           form=form)