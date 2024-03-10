# Pokemon API Test Suite

This test suite is designed to test the functionality of the Pokemon API (https://pokeapi.co/api/v2/).

## Setup

1. Clone the repository:

```commandline
git clone https://github.com/aamitd/matrix_assignment.git
```

2. Install the required dependencies:
```commandline
pip3 install requests
```

```commandline
pip3 install pytest
```


## Test Structure

The test suite is organized using the pytest framework. Test cases are defined within the `TestPokemon` class in the `test_pokemon.py` file.

### Fixtures

The test suite makes use of pytest fixtures to set up preconditions and share resources among test cases. The following fixtures are defined:

- `response`: Makes an HTTP GET request to the Pokemon API endpoint.
- `response_json`: Parses the JSON response obtained from the API request.
- `fire_index`: Finds the index of the 'fire' type Pokemon in the response.
- `fire_pokemon_url`: Retrieves the URL of the 'fire' type Pokemon.

### Test Cases

The test cases are categorized based on the functionality being tested:

- `test_task01`: Checks the status code, content type, and number of Pokemons returned by the API.
- `test_task02`: Verifies the presence of 'fire' type Pokemon and lists their names.
- `test_task03`: Tests the weights of specific 'fire' type Pokemon against expected values.

