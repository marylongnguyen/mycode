#/usr/bin/python3
  
import requests
import pprint

limit = '?limit=30'
URL = 'https://pokeapi.co/api/v2/pokemon/'

resp = requests.get(URL+limit)

pokemondata = resp.json()

print("pokemon api keys: ")
print(pokemondata.keys())

pokemon = pokemondata["results"]

print(type(pokemon))
print(pokemon)

for pokemon_name in pokemon:
    name = pokemon_name["name"]
    print(name)

#pprint.pprint(pokemon)

#print(pokemon.key())
#print(pokemon.values())
