__version__ = "0.5"

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "a": "pass",
    "b": "pass",
    "c": "pass",
    "d": "pass",
}

store = {}


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
    store[key] = request.data
    return ""


if __name__ == '__main__':
    app.run()
