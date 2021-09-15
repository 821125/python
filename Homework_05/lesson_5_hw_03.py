dic = {}
total = []

with open('employees_list.txt', 'r', encoding='utf-8') as f:
    print(f'\nread file "{f.name}":\n')
    for line in f:
        print(line, end='')
        s = line.split()
        dic[s[0]] = float(s[1])
    print('\n')

print('employees with salary less than 20 000.00:')
for el in dic:
    total.append(dic.get(el))
    if dic.get(el) < 20000.00:
        print(el)

print(f'\naverage salary = {round(sum(total) / len(dic), 2)}')
