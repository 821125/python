proceeds = int(input('Введите выручку организации в руб: '))
costs = int(input('Введите  издержки организации в руб: '))
if proceeds < costs:
    print('Ваша организация работает в убыток.')
    print('Ваш убыток составляет: ', proceeds - costs, 'руб.')
else:
    print('Ваша фирма работает с прибылью:', proceeds - costs, 'руб.')
    companyStaff = int(input('Введите количество сотрудников: '))
    print('Прибыль организации в расчете на сотрудника:', round((proceeds - costs) / companyStaff), 'руб.')
