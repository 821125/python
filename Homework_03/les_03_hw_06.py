def int_func(lst):
    """taking a string from small latin letters and returning it, but with a capital first letter"""

    return lst.title() if lst.islower() else '-= invalid input =-'


help(int_func)
print(int_func(input('input text: ')))
