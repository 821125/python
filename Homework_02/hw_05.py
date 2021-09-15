# реализация структуры "Рейтинг"

lst_rate = [7, 5, 3, 3, 2]
print('Текущий рейтинг', lst_rate)

digit = int(input("Введите число (или 00 для выхода): "))
while digit != 00:
    for el in range(len(lst_rate)):
        if lst_rate[el] == digit:
            lst_rate.insert(el + 1, digit)
            break
        elif lst_rate[0] < digit:
            lst_rate.insert(0, digit)
        elif lst_rate[-1] > digit:
            lst_rate.append(digit)
        elif lst_rate[el] > digit and lst_rate[el + 1] < digit:
            lst_rate.insert(el + 1, digit)
    print(f"текущий список - {lst_rate}")
    digit = int(input("Введите число "))
