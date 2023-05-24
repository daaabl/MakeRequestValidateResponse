import pytest
from config import URL
import requests

@pytest.fixture(scope="session")
def make_request():
    response = requests.get(url=URL)
    return response