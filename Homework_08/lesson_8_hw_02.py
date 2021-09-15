class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    divisible = int(input('input divisible: '))
    divider = int(input('input divider: '))
    if divider == 0:
        raise OwnError(f'\033[31mERROR: division by zero')
except ValueError:
    print('\033[31myou entered an invalid value')
except OwnError as err:
    print(err)
else:
    print(f'\033[32moperation completed, result = {divisible / divider}\033[0m')
