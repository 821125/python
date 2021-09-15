# test
f_obj = open('my_file_test.txt', 'w', encoding='utf-8')
f_obj.write('Test str 1\n')
f_obj.write('Test str 2\n')
f_obj.write('Test str 3\n')
f_obj.close()

with open('my_file.txt', 'w', encoding='utf-8') as f:
    while True:
        inp = input('Введите строку: ')
        if not inp:
            break
        f.write(f'{inp}\n')

