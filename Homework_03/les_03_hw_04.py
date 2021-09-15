def my_func_one(a, b):
    """
    function of exponentiation
    you need to enter two variables:
    number is a real positive integer
    degree is a real negative integer
    """

    print(f'{a} ** {b} = {round((a ** b), 2)}' if a > 0 and b < 0 else '-= invalid input =-')


def my_func_two(x, y):
    """function exponentiation"""

    result = x
    for _ in range(abs(y) - 1):
        result *= x
    print(f'{x} ** {y} = {round(1 / result, 2)}' if x > 0 and y < 0 else '-= invalid input =-')


help(my_func_one)
numbers_one = [2, 3, 4]
numbers_two = [-2, -3, -4]

# control values
print('\ncontrol values:')
for i in numbers_one:
    for j in numbers_two:
        print(f'{i} ** {j} = {round(pow(i, j), 2)}')

# static test my_func_one
print('\nstart of the static test my_func_one:')
for i in numbers_one:
    for j in numbers_two:
        my_func_one(i, j)

# static test my_func_two
print('\nstart of the static test my_func_two:')
for i in numbers_one:
    for j in numbers_two:
        my_func_two(i, j)

# manual test my_func_one:
print('\nstart of the manual test my_func_one:')
my_func_one(int(input('input number: ')), int(input('input degree: ')))

# manual test my_func_two:
print('\nstart of the manual test my_func_two:')
my_func_two(int(input('input number: ')), int(input('input degree: ')))
