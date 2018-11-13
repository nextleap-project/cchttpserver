import base64
import hashlib
import pytest
from cchttpserver import create_app


@pytest.fixture
def app(tmpdir):
    users = {
        "a": "pass",
        "b": "pass",
        "c": "pass",
        "d": "pass",
    }
    config = {"users": users,
              'dbdir': tmpdir.join("db").strpath}

    app = create_app(config)
    app.debug = True
    return app.test_client()


def get_key(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def test_put_invalid_login(app):
    creds = base64.b64encode(b'a:wrongpass').decode('utf-8')
    r = app.put('/' + get_key(b''), data=b'123', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 401
    creds = base64.b64encode(b'qwe:pass').decode('utf-8')
    r = app.put('/' + get_key(b''), data=b'123', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 401


def test_put_and_get_and_delete(app):
    datalist = [b'1'*40, b'2'*40]
    for data in datalist:
        creds = base64.b64encode(b'a:pass').decode('utf-8')
        r = app.put('/' + get_key(data), data=data, headers={'Authorization': 'Basic ' + creds})
        assert r.status_code == 200

    for data in datalist:
        r = app.get('/' + get_key(data))
        assert r.status_code == 200
        assert r.get_data() == data

    r = app.delete('/a/', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 200

    for data in datalist:
        r = app.get('/' + get_key(data))
        assert r.status_code == 404

    r = app.delete('/a/', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 200


def test_indicate_repetition(app):
    data = b"123"
    creds = base64.b64encode(b'a:pass').decode('utf-8')
    r = app.put('/' + get_key(data), data=data, headers={'Authorization': 'Basic ' + creds})
    r = app.put('/' + get_key(data), data=data, headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 202


def test_signal_conflict_on_overwrite_attempt(app):
    creds = base64.b64encode(b'a:pass').decode('utf-8')
    r = app.put('/' + get_key(b'123'), data=b"123", headers={'Authorization': 'Basic ' + creds})
    r = app.put('/' + get_key(b'123'), data=b"234", headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 409
