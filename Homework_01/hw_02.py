sec = int(input('Введите время в секундах: '))
hours = sec // 3600
minutes = (sec // 60) % 60
sec = sec % 60
print(hours, minutes, sec, sep=':')
