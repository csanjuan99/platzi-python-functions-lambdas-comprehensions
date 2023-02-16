def sum(a, b):
    return a + b


def hsum(a, b, f):
    return f(a, b)


sum_v2 = lambda a, b: a + b

print(hsum(1, 2, sum))
print(hsum(1, 2, sum_v2))
