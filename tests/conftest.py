import os

import pytest
from starlette.testclient import TestClient

from app.main import app

@pytest.fixture()
def testclient():

    with TestClient(app) as client:
        yield client