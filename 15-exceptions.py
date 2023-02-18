# suma = lambda x, y: x + (y * 2)
# assert suma(1, 2) == 3
# print(0/0)
# print("Fin del programa")
#
#
# age = int(input("Ingrese su edad: "))
# if age < 18:
#     raise Exception("No puede pasar")

try:
    print(0/0)
except ZeroDivisionError as e:
    print("Error: ", e)