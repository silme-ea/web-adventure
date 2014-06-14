from flask import render_template
from .forms import PromptField
from webadventure.app import app

@app.route('/prompt', methods=['GET', 'POST'])
def prompt():
    form = PromptField()
    return render_template('user/prompt.html',
                           form=form)