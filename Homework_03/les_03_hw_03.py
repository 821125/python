def my_func(arg_1, arg_2, arg_3):
    """function summation"""

    lst = [arg_1, arg_2, arg_3]
    lst.remove(min(lst))
    print(f'result: {sum(lst)}')


help(my_func)
# static test
print('\nstart of the static test:')
my_func(1, 2, 3)

# manual test
print('\nstart of the manual test:')
my_func(int(input('input number 1: ')), int(input('input number 2: ')), int(input('input number 3: ')))
