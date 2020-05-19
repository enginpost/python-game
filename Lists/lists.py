pets = ['reggie']
pets.append('birdy boy')
pets.insert(0,'rawf')
print('pets:', pets)
# ['rawf', 'reggie', 'birdy boy']
pets.reverse()
print('reversed pets: ',  pets)
# ['birdy boy', 'reggie', 'rawf']
sorted_pets = sorted(pets)
print('sorted: ',  sorted_pets)
print('reversed pets: ',  pets)
sorted_pets.reverse()
print('sorted pets reversed: ', sorted_pets)
last_pet = pets.pop()
first_pet = pets.pop(0)
print(last_pet,first_pet,pets)
ndx = 1
for pet in sorted_pets:
    print(f"pet #{ndx}: {pet.title()}")
    ndx+=1
