# variant 1
dic_one = {}
count = 0

f_obj = open('text_for_task_02.txt', 'r', encoding='utf-8')
print('\nvariant 1:')
for line in f_obj:
    count += 1
    dic_one[f'string {count}'] = len(line)
f_obj.close()

print(f'count of strings = {len(dic_one)}')
for key in dic_one:
    print(f'{key} - {dic_one[key]} symbols')

# variant 2
print('\nvariant 2:')
count = 0

with open('text_for_task_02.txt', 'r', encoding='utf-8') as f:
    for num, val in enumerate(f, 1):
        print(f'{num} string = {len(val)} symbols')
    print(f'total count of strings = {num}')
