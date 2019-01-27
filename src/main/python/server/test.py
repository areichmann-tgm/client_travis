import pytest

from server import rest


@pytest.fixture
def client():
    rest.app.testing = True
    #rest.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.MyStudents'
    client = rest.app.test_client()

    yield client


def test_get(client):
    res = client.get('/schueler')
    assert res.status_code == 200

def test_get(client):
    res = client.get('/schuelerA')
    assert res.status_code == 200

def test_delete(client):
    res = client.delete('/schuelerA',data={'schueler_id':'1000'})
    assert res.status_code == 200

def test_update(client):
    res = client.put('/schuelerA',data={'schueler_id':'1000','usernameX':'Adrian','emailX':'adrian@new.at','picture':'-'})
    assert res.status_code == 200

def test_insert(client):
    res = client.put('/schuelerA',data={'schueler_id': '10', 'usernameX': 'Nicht_Adrian', 'emailX': 'adrian@new.at', 'picture': '-'})
    assert res.status_code == 200

