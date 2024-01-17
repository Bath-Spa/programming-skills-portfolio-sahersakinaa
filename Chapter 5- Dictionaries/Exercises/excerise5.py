## Exercise 5: Pets :ballot_box_with_check:
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'wolf',
    'name': 'nick',
    'owner': 'saher',
    'weight': 35,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'panda',
    'name': 'tiffany',
    'owner': 'iman',
    'weight': 20,
    'eats': 'sugar cane',
}
pets.append(pet)

pet = {
    'animal type': 'rabbit',
    'name': 'dodo',
    'owner': 'dawood',
    'weight': 5,
    'eats': 'carrot',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")