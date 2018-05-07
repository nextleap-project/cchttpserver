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


@app.route('/', methods=["GET", "HEAD"])
def get():
    return store.get("last", None)


@app.route('/', methods=["PUT"])
@auth.login_required
def put():
    store["last"] = request.data
    return ""


if __name__ == '__main__':
    app.run()
