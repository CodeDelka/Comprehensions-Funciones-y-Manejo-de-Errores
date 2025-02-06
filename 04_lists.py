'''##agregar elementos a una lista o array
numbers = []
for element in range(1,11):
    numbers.append(element * 2)
print(numbers)    

##agregar elementos a una lista de manera comprimida
numbers_v2 = [element * 2 for element in range (1,11)]
print(numbers_v2)'''

###listas con condicional
numbers = []
for i in range(1,11):
 if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)

###listas con condicional (comprehesion)
numbers_v2 = [i * 2 for i in range (1,11) if i % 2 == 0]
print(numbers_v2)