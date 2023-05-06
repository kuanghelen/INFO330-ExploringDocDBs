from pymongo import MongoClient
import sqlite3

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

try:
    connection = sqlite3.connect("pokemon.sqlite")
    cursor = connection.cursor()

    # select all relevant pokemon fields
    pokemon_sql = "SELECT name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, abilities FROM imported_pokemon_data"
    results = cursor.execute(pokemon_sql)
    pokemon = results.fetchall()

    # insert pokemon, one-at-at-time, into the database collection
    for curr in pokemon:
        (name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, abilities) = curr   # define field variables
        types = [type1]     # store types
        if (type2 != ""):   # store type2 if the pokemon has it
            types.append(type2)
        
        # format the abilities and insert them into an array
        ability_str = abilities[1:len(abilities)-1].replace("'", "").replace(",","")
        ability_arr = ability_str.split()
        
        # create a document with specified fields
        insertion = {
            "name": name,
            "pokedex_number": int(pokedex_number) - 1, # pokedex_number will range [0,800]
            "types": types,
            "hp": int(hp),
            "attack": int(attack),
            "defense": int(defense),
            "speed": int(speed),
            "sp_attack": int(sp_attack),
            "sp_defense": int(sp_defense),
            "abilities": ability_arr
        }
        pokemonColl.insert_one(insertion)   # insert document into the collection
except Exception as e:
    print(e)
finally:
    connection.close()