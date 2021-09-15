with open('sum_numbers.txt', 'w', encoding='utf-8') as f:
    f.write(f'{input("input numbers: ")}')

with open('sum_numbers.txt', 'r', encoding='utf-8') as f:
    numbers = f.readline().split()
    total = sum(int(el) for el in numbers)
    print(f'sum of numbers in file "{f.name}" = {total}')
