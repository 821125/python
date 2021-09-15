n, x = int(input('Введите число n: ')), 0
for i in range(1, n + 1):
    x += int(str(n) * i)
print('Cуммa чисел n + nn + nnn + ... =', x)
