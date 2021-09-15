name = input('Введите ваше имя: ')
age = int(input('Сколько вам полных лет? '))
print('Добрый день, ', name, '!', sep='')
height = float(input('Введите свой рост в м (например 1.65): '))
weight = float(input('Введите свой вес в кг (например 50.7): '))
if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print('Ошибочные входные данные')
else:
    bmi = round(weight / height ** 2, 2)
    print('Ваш индекс массы тела: ', bmi)
    if bmi < 18.5:
        description = 'недостаточная масса тела.'
    elif 18.5 <= bmi <= 24.99:
        description = 'нормальная масса тела.'
    elif 25 < bmi <= 29.99:
        description = 'избыточная масса тела.'
    else:
        description = 'ожирение'
    print('У вас', description)
