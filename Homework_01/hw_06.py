a, b, c = int(input('Введите результать 1-го дня: ')), int(input('Введите планируемый результат: ')), 1
print('Результат:')
print('1 -й день:', a)
while True:
    a *= 1.1
    c += 1
    print(c, '-й день:', round(a, 2))
    if a >= b:
        break
print('Ответ: на ', c, '-й день спортсмен достиг результата - не менее ', round(a), ' км.', sep='')
