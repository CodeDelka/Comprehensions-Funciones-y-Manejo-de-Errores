##union de un conjunto
set_a = {'col', 'mex','bol'}
set_b = {'pe', 'bol'}

##opcion1 con el metodo
set_c = set_a.union(set_b)
print(set_c)
#opcion2 con el operador |
print(set_a | set_b)

#intersección de un conjunto
#opcion1 con el metodo
set_c = set_a.intersection(set_b)
print(set_c)
#opcion 2 con el operador &
print(set_a & set_b)

##diferencias de un conjunto
#opcion1 con el metodo
set_c = set_a.difference(set_b)
print(set_c)
#opcion2 con el operador -
print(set_a - set_b)

#diferencia simetrica de un conjunto
#opcion1 con el metodo
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#opcion2 con el operador ^
print(set_a ^ set_b)