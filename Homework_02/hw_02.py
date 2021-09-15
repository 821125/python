# реализация обмена значений соседних элементов
lst = input().split()
for i in range(1, len(lst)):
    if i % 2:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
print(lst)
