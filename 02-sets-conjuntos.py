# Los conjuntos no tienen orden,
# no se repetir elementos y se pueden modificar
set_countries = {
    'Brasil',
    'Argentina',
    'Colombia',
}
print(set_countries)
set_countries.add('Peru')  # modificando un conjunto
print(set_countries)

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_numbers)
set_numbers.add(11)  # modificando un conjunto
print(set_numbers)

set_types = {0, 'Hola', 2.5, True, (1, 2, 3)}
print(set_types)

set_from_string = set('Hola Mundoo')  # note que hay doble o, no se repite en el set
print(set_from_string)

set_from_tuples = set(('abc', 'def', 'ghi', 'abc'))
print(set_from_tuples)

# modificando conjuntos
size = len(set_countries)
print(size)
set_countries.add('Chile')  # agrega un elemento al conjunto
print(set_countries)
set_countries.remove('Chile')  # elimina un elemento del conjunto y da error si no encuentra el elemento
print(set_countries)
set_countries.discard('Colombia')  # elimina pero no da error si no encuentra el elemento
print(set_countries)
set_countries.update(['Chile', 'Ecuador', 'Venezuela'])
print(set_countries)
set_countries.clear()  # elimina todos los elementos del conjunto
print(set_countries)

# operaciones con conjuntos
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union = set_a.union(set_b)  # union de conjuntos sin repetir si existe
# union = set_a | set_b  # otra forma de hacer union
print(union)
intersection = set_a.intersection(set_b)  # interseccion de conjuntos, me trae los elementos que se repiten
# intersection = set_a & set_b  # otra forma de hacer interseccion
print(intersection)
difference = set_b.difference(set_b)  # diferencia de conjuntos, me trae los elementos que no se repiten
# difference = set_a - set_b  # otra forma de hacer diferencia
print(difference)
symmetric_difference = set_a.symmetric_difference(set_b)  # diferencia simetrica de conjuntos, me trae los elementos que no se repiten
# symmetric_difference = set_a ^ set_b  # otra forma de hacer diferencia simetrica
print(symmetric_difference)
