from itertools import count, cycle
from sys import argv

script_name, num = argv
x = 0

print()
print('script name: ', script_name)
print('num: ', num)
print()

print('iteration of integers:')
for el in count(3):
    if el > 10:
        break
    else:
        print(el, end=' ')

print('\n\niteration of elements from list:')
for el in cycle([11, 22, 33]):
    if x > 10:
        break
    print(el, end=' ')
    x += 1
print()
