import json

lst = []
dic = {}
total, count = 0, 0

with open('firms.txt', 'r', encoding='utf-8') as f:
    for el in f:
        lst += [el[:-2].split()]
    for el in lst:
        dic[el[0]] = int(el[2]) - int(el[3])
        if dic[el[0]] > 0:
            total += dic[el[0]]
            count += 1

with open('firms.json', 'w') as write_f:
    json.dump([dic, {'average_profit': round(total / count, 2)}], write_f)
