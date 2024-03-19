def f(x):
    try:
        return x**2
    except TypeError as err:
        print(err)

def g(x):
    return x**2

f('2') # g('2')

print(g(f(4)))

