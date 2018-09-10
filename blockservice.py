__version__ = "0.5"

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from dummy_store import DummyStore


def create_app():
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    users = {
        "a": "pass",
        "b": "pass",
        "c": "pass",
        "d": "pass",
    }

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
