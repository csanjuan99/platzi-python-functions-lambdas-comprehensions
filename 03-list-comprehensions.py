numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_v1 = []
for number in range(1, 11):
    numbers_v1.append(number)
print(numbers_v1)

numbers_v2 = [number for number in range(1, 11)]
print(numbers_v2)

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

even_numbers_v2 = [number for number in numbers if number % 2 == 0]
print(even_numbers_v2)
