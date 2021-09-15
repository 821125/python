def my_func():
    """function summation"""

    total = 0
    flag = True
    while flag:
        numbers = (input('input numbers (or type Q for exit): ').split())
        for i in numbers:
            if i.upper() == 'Q':
                flag = False
                break
            else:
                total += int(i)
        print(total)


help(my_func)
my_func()
