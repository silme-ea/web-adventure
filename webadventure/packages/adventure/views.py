from flask import Blueprint, render_template
from .forms import PromptField
from .api import start_new_game, get_last_output, do_command

bp = Blueprint('prompt', __name__, url_prefix='/adventure')

#temporary global init of the game for test purposes
#TODO: should be removed and develop separate initialisations for each user
game = start_new_game()


@bp.route('/prompt/', methods=['GET', 'POST'])
def prompt_view():
    form = PromptField()
    output = get_last_output(game)

    if form.validate_on_submit():
        output = do_command(game, form.prompt.data)
        form.prompt.data = ''

    return render_template('adventure/prompt.html',
                           form=form,
                           game_output=output)
