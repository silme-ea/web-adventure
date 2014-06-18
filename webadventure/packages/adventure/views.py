import json

from jinja2 import Markup
from flask import Blueprint, render_template, request, Response

from .forms import PromptField
from .api import start_new_game, get_last_output, do_command

bp = Blueprint('prompt', __name__, url_prefix='/adventure')

#temporary global init of the game for test purposes
#TODO: should be removed and develop separate initialisations for each user
game = start_new_game()


@bp.route('/next/', methods=('POST', ))
def api_next():
    form = PromptField(request.form)
    output = do_command(game, form.prompt.data)
    output = Markup('<p class="prompt-answer">%s</p>' % output)
    print(output)

    return Response(json.dumps(output, ensure_ascii=False, indent=4), mimetype='application/json')


@bp.route('/prompt/', methods=('GET', 'POST'))
def prompt_view():
    form = PromptField()
    output = get_last_output(game)

    return render_template('adventure/prompt.html',
                           form=form,
                           game_output=output)
