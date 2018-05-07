import base64
import pytest
import blockservice


@pytest.fixture
def app():
    return blockservice.app.test_client()


def test_put_invalid_login(app):
    creds = base64.b64encode(b'a:wrongpass').decode('utf-8')
    r = app.put('/', data=b'123', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 401
    creds = base64.b64encode(b'qwe:pass').decode('utf-8')
    r = app.put('/', data=b'123', headers={'Authorization': 'Basic ' + creds})
    assert r.status_code == 401


def test_put_and_get(app):
    for data in (b"123", b"456"):
        creds = base64.b64encode(b'a:pass').decode('utf-8')
        r = app.put('/', data=data, headers={'Authorization': 'Basic ' + creds})
        assert r.status_code == 200

        r = app.get("/")
        assert r.status_code == 200
        assert r.get_data() == data
