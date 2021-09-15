seasons = {
    12: 'winter', 1: 'winter', 2: 'winter',
    3: 'spring', 4: 'spring', 5: 'spring',
    6: 'summer', 7: 'summer', 8: 'summer',
    9: 'autumn', 10: 'autumn', 11: 'autumn'
}
month = int(input('Введите номер месяца: '))
while 0 > month or month > 12:
    print('ошибочные данные')
    month = int(input('введите номер месяца в диапазона от 1 до 12: '))
else:
    print('решение 1 - через словарь:', end=' ')
    print(seasons.get(month))
    print('решение 2 - через списки:', end=' ')
    if month in [12, 1, 2]:
        print('winter')
    elif month in [3, 4, 5]:
        print('spring')
    elif month in [6, 7, 8]:
        print('summer')
    elif month in [9, 10, 11]:
        print('autumn')
