from collections import deque

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

dic = {
    'HotSpot': [20.0, 25.5, 30.4, 35.4],
    'Atlanta': [55.0, 40.4, 40.5, 25.5],
    'RedArmy': [55.0, 25.3, 45.2, 50.3],
    'AquaTop': [15.0, 55.2, 10.1, 25.2]
}

val = 0

for i in dic:
    dic.get(i).append(round(sum(dic.get(i)) / 4, 1))
    val += dic.get(i)[4]

for i in dic:
    if dic.get(i)[4] > val / len(dic):
        print(f'Profit {i} company is higher than average profit')

for i in dic:
    if dic.get(i)[4] > val / len(dic):
        print(f'Profit {i} company is lower than average profit')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


a, b = ''.join(['A', '2']), ''.join(['C', '4', 'F'])

# простые способы

print(hex(int(a, 16) + int(b, 16)))
print(hex(int(a, 16) * int(b, 16)))

print(hex(eval(f'0x{a} + 0x{b}')))
print(hex(eval(f'0x{a} * 0x{b}')))

# не ищем легких путей...

a, b = ['A', '2'], ['C', '4', 'F']
hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def s_hex(x, y):
    result = deque()
    transfer = 0

    x, y = (deque(y), deque(x)) if len(y) > len(x) else (deque(x), deque(y))
    while x:
        if y:
            res = hex_num[x.pop()] + hex_num[y.pop()] + transfer
        else:
            res = hex_num[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')

    return list(result)


def m_hex(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for el in range(len(y)):
        m = hex_num[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[el].appendleft(m * hex_num[x[j]])
        for _ in range(el):
            spam[el].append(0)
    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer + sum(spam[j].pop() for j in range(len(spam)) if spam[j])
        if res < 16:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res % 16])
            transfer = res // 16
    if transfer:
        result.appendleft(hex_num[transfer])

    return list(result)


print(s_hex(a, b), m_hex(a, b))
