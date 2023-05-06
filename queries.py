from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu". (1pt)
print('There is ' + str(pokemonColl.count_documents({"name": "Pikachu"})) + ' Pokemon named "Pikachu":')
q1 = pokemonColl.find({"name": "Pikachu"})
for row in q1:
    print(row)
print()

# Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
print("There are " + str(pokemonColl.count_documents({"attack": {"$gt": 150}})) + 
      " Pokemon with an attack greater than 150")
q2 = pokemonColl.find({"attack": {"$gt": 150}})
for row in q2:
    print(row)
print()

# Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)
print('There are ' + str(pokemonColl.count_documents({"abilities": {"$in": ["Overgrow"]}})) + 
      ' Pokemon with an ability of "Overgrow":')
q3 = pokemonColl.find({"abilities": {"$in": ["Overgrow"]}})
for row in q3:
    print(row)
