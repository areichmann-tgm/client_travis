import pytest

from server import rest


@pytest.fixture
def client():
    rest.app.testing = True
    #rest.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.MyStudents'
    client = rest.app.test_client()

    yield client


def test_ping(client):
    res = client.get('/schueler')
    assert res.status_code == 200

def test_ping2(client):
    res = client.get('/schuelerA')
    assert res.status_code == 200

def test_delete(client):
    res = client.delete('/schuelerA',data={'schueler_id':'1000'})
    assert res.status_code == 200