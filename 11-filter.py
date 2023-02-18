numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filter_numbers)
print(numbers)


def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda word: len(word) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)