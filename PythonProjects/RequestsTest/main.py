import requests

URL = "https://api.pokemonbattle.ru"
TOKEN = "afe8d7d0ec2867e6bab3e5ab9feada9f"
HEADER = {"Content-Type" : "application/json",  "trainer_token" : TOKEN,}
Body_creating = {
    "name" : "RedStor",
    "photo_id": 69
}
Body_pokemons ={
    "pokemon_id": "129408",
    "name": "SNICH",
    "photo_id": 69
}
Body_pokebol ={
    "pokemon_id": "129408"
}

"""response = requests.post(url = f"{URL}/v2/pokemons", headers = HEADER, json = Body_creating)
print(response.text)"""

"""response_change = requests.put(url = f"{URL}/v2/pokemons", headers = HEADER, json = Body_pokemons)
print(response_change.text)"""

"""response_pokebol = requests.post(url = f"{URL}/v2/trainers/add_pokeball", headers = HEADER, json = Body_pokebol)
print(response_pokebol.text)"""
