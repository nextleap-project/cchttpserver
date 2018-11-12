__version__ = "0.6.0.dev1"

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from dummy_store import DummyStore


def create_app(test_config=None):
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config['users'] = test_config.get('users')

    users = app.config.get('users')
    store = DummyStore()

    @auth.get_password
    def get_pw(username):
        if username in users:
            return users.get(username)
        return None

    @app.route('/<key>', methods=["GET", "HEAD"])
    def get(key):
        return store.get(key, None)

    @app.route('/<key>', methods=["PUT"])
    @auth.login_required
    def put(key):
        value = store.get(key, None)
        if value:
            if value == request.data:
                return "", 202
            else:
                return "", 409
        writer = store.writer(auth.username())
        writer.set(key, request.data)
        return ""

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
