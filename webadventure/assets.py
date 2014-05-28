import os.path as op
import platform

from flask import url_for
from flask.ext.assets import Resolver, Environment

from webadventure.app import app


class CustomResolver(Resolver):
    def resolve_output_to_url(self, target):
        return url_for('static', filename=target)


class CustomEnvironment(Environment):
    resolver_class = CustomResolver


assets = CustomEnvironment(app)


def init(app):
    assets.debug = app.config.get('ASSETS_DEBUG', False)
    assets.auto_build = app.config.get('ASSETS_TRACK', False)

    if platform.system() == 'Windows':
        assets.config['less_bin'] = 'lessc.cmd'
        assets.config['uglifyjs_bin'] = 'uglifyjs.cmd'

    path = op.abspath(op.join(op.dirname(__file__), '..', 'frontend'))
    assets.append_path(path, '/dev_static')
    assets.from_yaml(op.join(path, 'assets.yml'))
