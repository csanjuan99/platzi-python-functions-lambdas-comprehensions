numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def per_two(number):
    return number / 2


numbers_per_two = map(per_two, numbers)

print(list(numbers_per_two))

ingredients = ['Carne', 'Pollo', 'Pescado']
meals = ['Hamburguesa', 'Pechuga', 'Filete']

process = map(lambda x, y: f'{x} se transformo en {y}', ingredients, meals)
print(list(process))

before_transform_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transform_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def transforming(a, b):
    return a / b


print(list(map(transforming, before_transform_numbers, transform_numbers)))
