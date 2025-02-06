import random
countries = ['col', 'mex', 'bol', 'pe']
population_v2 = { i: random.randint(1,100) for i in countries }
print(population_v2)

result = {i: population for (i, population) in population_v2.items() if population > 50}
print(result)

##dict comprehension with condicional

text = 'hola, Soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou'}

print(unique)