# test_run.py

import os
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Verifica que la ruta de inicio responda con el código 200"""
    response = client.get('/')
    assert response.status_code == 404

# Agrega más pruebas según sea necesario

