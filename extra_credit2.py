# Summary of algorithm changes
#   - implemented a counting system of stats wins
#   - a pokemon earns 1 point for each stat category that they beat their opponent in
#   - if a pokemon has better overall stats wins than their opponent, they win the battle
#   - if battle pokemon have the same number of stats wins, a random pokemon will win

import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    # keep track of wins based on stats comparisons
    pokemon1_wins = 0
    pokemon2_wins = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            pokemon1_wins += 1  # pokemon1 has a better stat in this category
            print(pokemon1['name'] + " has the advantage in " + stat)
        elif pokemon2[stat] > pokemon1[stat]:
            pokemon2_wins += 1  # pokemon2 has a better stat in this category
            print(pokemon2['name'] + "'s " + stat + " is superior")

    # testing
    # print(pokemon1['name'] + ": " + str(pokemon1_wins))
    # print(pokemon2['name'] + ": " + str(pokemon2_wins))

    if pokemon1_wins > pokemon2_wins:   # pokemon1 has better overall stats -> they win
        print("Battle results: " + pokemon1['name'])
    elif pokemon1_wins < pokemon2_wins: # pokemon2 has better overall stats -> they win
        print("Battle results: " + pokemon2['name'])
    else:                               # battle pokemon tie in stats -> randomize winner
        winner = random.randrange(2)
        if winner == 0: print("Battle results: " + pokemon1['name'])
        if winner == 1: print("Battle results: " + pokemon2['name'])

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
