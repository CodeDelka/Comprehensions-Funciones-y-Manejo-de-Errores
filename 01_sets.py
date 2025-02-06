set_countries = {'col', 'mex', 'bol','col'}
##en un conjunto no puede haber documentos duplicados.
print(set_countries)
print(type(set_countries))


set_numbers = {1,2,2,3,44}
print(set_numbers)

set_types = {1, 'hola', False,12.2}
print(set_types)
print(type(set_types))

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'abc', 'cbv', 'as'))
print(set_from_tuples)

numbers = [1,2,3,4,5,1,2,3,4,5]
set_numbers2 = set(numbers)
print(set_numbers2)

unique_numbers = list(set(numbers))
print(unique_numbers)