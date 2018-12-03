import pytest
import main.python.server.rest
from flask import  url_for
from flask import Flask

@pytest.fixture
def client():
    main.python.server.rest.app.testing = True
    client = main.python.server.rest.app.app.test_client();
    yield client


def test_ping(client):
    res = client().get('/schueler')
    assert res.status_code == 200

