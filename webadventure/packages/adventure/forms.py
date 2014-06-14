from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class PromptField(Form):
    prompt = TextField('prompt', validators=[Required()])
