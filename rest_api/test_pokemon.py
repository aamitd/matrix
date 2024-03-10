import requests
import pytest


@pytest.fixture(scope='module', autouse=True)
def response():
    return requests.get(url)


@pytest.fixture(scope='module', autouse=True)
def response_json(response):
    return response.json()


@pytest.fixture(scope='module', autouse=True)
def fire_index(response_json):
    for index, pokemon in enumerate(response_json['results']):
        if pokemon['name'] == 'fire':
            return index


@pytest.fixture(scope='module', autouse=True)
def fire_pokemon_url(response_json, fire_index):
    return response_json['results'][fire_index]['url']


url = 'https://pokeapi.co/api/v2/type'
constant_pokemons = 20


class TestPokemon:
    @pytest.mark.usefixtures("response_json")
    def test_task01(self, response, response_json):
        # Check if the status code is 200
        assert response.status_code == 200
        # Check if the content type is correct
        assert response.headers['content-type'] == 'application/json; charset=utf-8'
        # Check if the number of pokemons matches the constant
        assert response_json['count'] == constant_pokemons

    print()

    @pytest.mark.usefixtures("response_json", "fire_index")
    def test_task02(self, response, response_json, fire_index):
        assert fire_index is not None
        fire_pokemon = response_json['results'][fire_index]
        # Check if the pokemon at the stored index is 'fire' type
        assert fire_pokemon['name'] == 'fire'
        print(f"The index of the fire pokemon is: {fire_index}")
        print(fire_pokemon)

        print()

        # Get the URL of the 'fire' type pokemon
        fire_pokemon_url = fire_pokemon['url']

        # Make a request to get details of the 'fire' type pokemon
        response_fire_pokemon = requests.get(fire_pokemon_url)
        response_fire_json = response_fire_pokemon.json()

        # print(response_fire_json['pokemon'][0]['pokemon'])
        pokemon_fire_names_lst = []
        i = 0 # to assert that i have 103 pokemons in the list.
        for pokemon_entry in response_fire_json['pokemon']:
            pokemon_fire_name = pokemon_entry['pokemon']['name']
            pokemon_fire_names_lst.append(pokemon_fire_name)
            i += 1
        print(pokemon_fire_names_lst)
        print(f"You have {i} pokemons in the list.")

        assert 'charmander' in pokemon_fire_names_lst
        assert 'bulbasaur' not in pokemon_fire_names_lst

    def test_task03(self, response, response_json, fire_index, fire_pokemon_url):
        assert fire_index is not None

        response_fire_pokemon = requests.get(fire_pokemon_url)
        response_fire_json = response_fire_pokemon.json()

        weights = {
            "charizard-gmax": 10000,
            "cinderace-gmax": 10000,
            "coalossal-gmax": 10000,
            "centiskorch-gmax": 10000,
            "groudon-primal": 9997
        }

        for pokemon_entry in response_fire_json['pokemon']:
            pokemon_fire_name = pokemon_entry['pokemon']['name']
            if pokemon_fire_name in weights:
                if pokemon_fire_name == "charizard-gmax":
                    base_url = pokemon_entry['pokemon']['url']
                    response_base_url = requests.get(base_url)
                    response_base_url_json = response_base_url.json()
                    # Get the weight of the pokemon
                    pokemon_weight = response_base_url_json['weight']
                    # Check if the weight matches the expected weight from the weights dictionary
                    assert pokemon_weight == weights[pokemon_fire_name]
                    print("Good")
