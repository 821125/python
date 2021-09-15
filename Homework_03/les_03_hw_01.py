import random


def my_div(divisible, divisor):
    """returns the result of dividing two numbers"""

    try:
        result = round((int(divisible) / int(divisor)), 2)
        return f'the result of the division {divisible} / {divisor} = ', result
    except TypeError:
        return '-= input number =-'
    except ValueError:
        return '-= input number =-'
    except ZeroDivisionError:
        return '-= invalid input =-'


help(my_div)
# static test
print('start of the static test:')

lst_one = [-10, -5, 0, 10, 70, 'ab', -20, 8.2, 2.1, 8]
lst_two = [-5, -10, 10, 0, 35, 'dc', 1.2, -12, 2, 1.1]

for i in range(10):
    print(*my_div(lst_one[i], lst_two[i]))

# dynamic test
print('\nstart of the dynamic test:')

for i in range(1, 10 + 1):
    print(*my_div(round(random.uniform(-100, 100), 2), random.randint(-100, 100)))

# manual test
print('\nstart of the manual test:')

while True:
    if input('press Enter (or type anything) to continue or type Q for exit: ').upper() == 'Q':
        break
    else:
        print(*my_div(input('enter the divisible: '), input('enter the divisor: ')))
