lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_one = []

for i in range(len(lst) - 1):
    if lst[i + 1] > lst[i]:
        lst_one.append(lst[i + 1])

print(lst_one)
