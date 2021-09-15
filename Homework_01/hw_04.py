num, maxNum = int(input('Введите целое положительное число n: ')), 0
num = int(num)
if num < 0:
    print('Вы ввели отрицательное число.')
else:
    while num:
        if num % 10 > maxNum:
            maxNum = num % 10
        num = num // 10
    print('Самая большая цифра в числе n:', maxNum)
