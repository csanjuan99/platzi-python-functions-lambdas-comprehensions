def volume(width=1, height=1, depth=1):
    return width * height * depth, width, 'Hola'

print(volume(2, 3, 4))
volume, width, text = volume(2, 3, 4)  # Unpacking in order to return values
print(volume)
print(width)
print(text)