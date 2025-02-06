'''##agregar elementos a un diccionario
dict = {}
for i in range (1,5):
    dict[i] = i*2
print(dict)    

##agregar elementos a un diccionario con comprehension
dict_v2 = {i:i * 2 for i in range (1,5)}
print(dict_v2)

#diccionario con ciclos
import random
countries = ['col', 'mex', 'bol', 'pe']
population = { }
for i in countries:
    population[i] = random.randint(1,100)
print(population)    

#diccionario con ciclos comprehesion
population_v2 = { i: random.randint(1,100) for i in countries }
print(population_v2)'''

##diccionario 
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

##diccionario comprehension

new_dict = {names: ages for (names,ages) in zip(names, ages)}
print(new_dict)