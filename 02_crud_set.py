set_countries = {'col', 'mex', 'bol'}
##tamaño de un conjunto
size = len(set_countries)
print(size)

##verificar si hace parte de un conjunto
print('col' in set_countries)
print('peru' in set_countries)

##agregar elemento a un conjunto
set_countries.add('peru')
print(set_countries)
print('col' in set_countries)
print('peru' in set_countries)

#actualizar un conjunto
set_countries.update({'arg', 'ecua', 'peru'})
print(set_countries)

##eliminar dato de un conjunto (solo un dato a la vez)
set_countries.remove('peru')
print(set_countries)

##segundo metodo para eliminar(un dato a la vez)
set_countries.discard('col')
print(set_countries)

##limpiar conjunto(borrar todo)
set_countries.clear()
print(set_countries)