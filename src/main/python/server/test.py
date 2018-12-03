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
