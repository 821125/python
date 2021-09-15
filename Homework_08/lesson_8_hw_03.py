class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = []

while True:
    el = input('input a number or "Q" for exit: ').upper()
    if el == 'Q':
        print(f'\033[34mprogram completed\033[0m')
        break
    else:
        try:
            if el.isdigit():
                lst.append(el)
            else:
                raise OwnError(f'\033[31mERROR: you did not enter a number\033[0m')
        except OwnError as err:
            print(err)
        finally:
            print(f'\033[33mcurrent list: {lst}\033[0m')
