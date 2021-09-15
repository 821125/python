lst = []
dic = {}

with open('lessons.txt', 'r', encoding='utf-8') as f:
    for el in f:
        lst += [el.split()]
    for el in lst:
        dic[el[0]] = el[1:]
    for key in dic:
        total = 0
        for el in dic.get(key):
            if el[:el.find('(')].isdigit():
                total += int(el[:el.find('(')])
        dic[key] = total

print(dic)
