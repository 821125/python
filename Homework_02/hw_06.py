# реализация структуры "Товары"

base = []
name, price, quantity, units = [], [], [], []
el = ()
my_dict = {}

my_base_dict = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед.': []
}

while True:
    print('введите 00 для выхода')
    number = int(input('введите номер товара: '))
    if number == 000:
        break
    else:
        my_dict = {
            'название': input('введите название: '),
            'цена': int(input('введите цену: ')),
            'количество': int(input('введите количество: ')),
            'ед': input('введите единицы: ')
        }
        el = number, my_dict
        base.append(el)

for i in base:
    name.append(i[1].get('название'))
    price.append(i[1].get('цена'))
    quantity.append(i[1].get('количество'))
    units.append(i[1].get('ед'))

my_analys = {
    'название': set(name),
    'цена': set(price),
    'количество': set(quantity),
    'ед': set(units)
}

print()

while True:
    print('введите a для вывода аналитики', 'введите s для вывода структуры', 'введите q для выхода', sep='\n')
    control = input().lower()
    if control == 'q':
        break
    elif control == 's':
        for i in base:
            print(i)
        print()
    elif control == 'a':
        for i in my_analys:
            print(i, my_analys.get(i))
        print()
