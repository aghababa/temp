def f(x):
    try:
        return x**2
    except TypeError as err:
        print(err)

def g(x):
    return x**2

f('2') # g('2')

print(g(10))

<<<<<<< HEAD
print(f(5))
=======
print(f(5))

print("Hi")

print('I like food')


