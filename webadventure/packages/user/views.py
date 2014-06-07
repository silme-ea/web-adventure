from flask import Blueprint, flash, request, render_template, url_for, redirect
from flask.ext.login import login_user, logout_user

from . import forms

from webadventure.database import db


bp = Blueprint('user', __name__, url_prefix='/user')


# Authentication
@bp.route('/register/', methods=('GET', 'POST',))
def register():
    form = forms.RegisterForm()

    if form.validate_on_submit():
        user = form.get_user()
        db.session.add(user)
        db.session.commit()

        flash('User account was created. Please wait for our admin to activate you.')

        return redirect(url_for('core.index'))

    return render_template('user/register.html', form=form)


@bp.route('/login/', methods=['GET', 'POST'])
def login_view():
    next = request.args.get('next')

    form = forms.LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.cached_user)
        return redirect(next)

    return render_template('user/login.html', form=form, next=next)


@bp.route('/logout/')
def logout_view():
    logout_user()
    return redirect(url_for('core.index'))
