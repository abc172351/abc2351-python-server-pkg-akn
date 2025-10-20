import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from main import app


@pytest.fixture()
def abc2351_python_api():
    with app.test_client() as abc2351_python_api:
        yield abc2351_python_api


def test_index(abc2351_python_api):
    response = abc2351_python_api.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, World!"
