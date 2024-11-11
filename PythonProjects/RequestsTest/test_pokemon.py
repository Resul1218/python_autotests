import requests
import pytest

URL = "https://api.pokemonbattle.ru"
TOKEN = "afe8d7d0ec2867e6bab3e5ab9feada9f"
HEADER = {"Content-Type" : "application/json",  "trainer_token" : TOKEN,}
TRAINER_ID = "9028"

def test_status_code():
    response = requests.get(url = f"{URL}/v2/trainers",)
    assert response.status_code == 200

def test_my_name():
    response_get = requests.get(url = f"{URL}/v2/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "RedStor"