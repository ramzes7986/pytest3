import requests
import pytest

from src.enums.global_enums import headers
from src.enums.global_enums import global_url


@pytest.fixture
def test_authorization():

    url = global_url+"/api/admin/auth/signin"
    json = {
        "email": "admin@admin.com",
        "password": "fM57Ls8rxVNE8gTD"
    }

    res = requests.post(url=url, json=json, headers=headers)
    token = res.json()["data"]
    return "Bearer"+token

