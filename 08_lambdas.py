def sumatory(a, b):
    return a + b


sum = lambda a=1, b=2: a + b

full_name = lambda name, lastname: f'Your fullname is {name} {lastname}!'
my_fullname = full_name('Carlos', 'Sanjuan')
print(sum())
print(full_name('Carlos', 'Sanjuan'), 'without text executing function')
print(my_fullname, 'with text')

