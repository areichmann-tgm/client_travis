import pytest
import main.python.server.rest
from flask import  url_for
from flask import Flask

@pytest.fixture
def client():
    main.python.server.rest = True
    yield client


def test_ping(client):
    res = client().get('/todos/schueler1')
    assert res.status_code == 200

