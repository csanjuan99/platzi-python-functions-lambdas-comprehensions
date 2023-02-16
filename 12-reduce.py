from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reduce_numbers = reduce(lambda counter, item: counter + item, numbers)
print(reduce_numbers)

 