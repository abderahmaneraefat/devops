# tests/test_app.py
import pytest
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
