import json

from jinja2 import Markup
from flask import Blueprint, render_template, request, Response

from .forms import PromptField
from .api import start_new_game, get_last_output, do_command, get_current_score, load_last_game

bp = Blueprint('prompt', __name__, url_prefix='/adventure')

#temporary global init of the game for test purposes
#TODO: should be removed and develop separate initialisations for each user
game = start_new_game()
#test loading game from file; comment line above and uncomment line below to test this feature
#game = load_last_game('./webadventure/packages/adventure/tests/testsave')

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
    output = Markup('<p class="prompt-answer">%s</p>' % output)

    return render_template('adventure/prompt.html',
                           form=form,
                           game_output=output,
                           score=get_current_score(game))
