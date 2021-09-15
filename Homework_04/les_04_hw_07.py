from math import factorial

n = 5


def fact(arg):
    """calculates the factorial of a number"""
    f = 1
    for i in range(1, arg + 1):
        f *= i
        yield f


help(fact)
print(f'test output (use factorial()): {[factorial(el) for el in range(1, n + 1)]}')
print(f'\n{[el for el in fact(n)]}')
