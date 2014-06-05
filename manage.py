from webadventure.app import app, init
from opster import command, dispatch

def _expose_dev_static(app):
    import os.path as op
    from flask import send_from_directory

    path = op.abspath(op.join(op.dirname(__file__), 'frontend'))

    @app.route('/dev_static/<path:filename>')
    def custom_static(filename):
        return send_from_directory(path, filename)


@command()
def devserver(
        bind=('b', '0.0.0.0', 'Bind address'),
        port=('p', 8000, 'Port number'),
        debug=('d', True, 'Debug mode'),
        cfg=('c', None, 'Override settings file')):
    app.debug = debug

    init(cfg or 'webadventure.settings')
    _expose_dev_static(app)
    app.run(bind, port)


@command()
def dbcreate():
    init('webadventure.settings')

    with app.test_request_context():
        from webadventure.database import create_all
        create_all()


@command(usage='')
def shell(no_ipython=('', False, 'do not use IPython')):
    '''Start a new interactive Python session
    '''
    init('webadventure.settings')

    with app.test_request_context():
        banner = 'Interactive shell\n'

        try:
            from IPython import embed
        except ImportError:
            pass
        else:
            try:
                import sys
                if sys.platform == 'win32':
                    import pyreadline
            except ImportError:
                banner = ('There is IPython installed on your system, '
                          'but no pyreadline\n' + banner)
            else:
                embed(banner1=banner)
                return
        from code import interact
        interact(banner)


if __name__ == '__main__':
    dispatch()
