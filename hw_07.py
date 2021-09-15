# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random
import timeit

lst = [random.randint(-100, 100) for _ in range(20)]
print(f'array:\n{lst}')

start_time = timeit.default_timer()


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False
        if flag == True:
            break
    return array


print(f'\nbubble_sort:\n{bubble_sort(lst)}')
print('time:', timeit.default_timer() - start_time, '\n')  # time: 9.120000000001349e-05

start_time = timeit.default_timer()

def bubble_sort_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array


print(f'bubble_sort_smart:\n{bubble_sort_smart(lst)}')
print('time:', timeit.default_timer() - start_time, '\n')  # time: 6.88000000000355e-05

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

lst = [random.randint(0, 50) for _ in range(25)]


def merge_sort(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_list(left_part, right_part)

def merge_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


print(f'merge_sort:\n{merge_sort(lst)}')

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# решение 1 - через сортировку в новый список со вложенными списками
m = random.randint(1, 9)
lst = [random.randint(0, 9) for _ in range(2 * m + 1)]
lst_sort = [[], [], []]

med = sum(lst) // len(lst)

for i in lst:
    if i < med:
        lst_sort[0].append(i)
    elif i == med:
        lst_sort[1].append(i)
    else:
        lst_sort[2].append(i)

lst_sort_one = lst_sort[0] + lst_sort[1] + lst_sort[2]

print()
print(f'{med          = }')
print(f'{lst          = }')
print(f'{lst_sort_one = }')

# решение 2 - через сортировку в новый список с флагом
lst_sort_two = []
flag = 0

for i in lst:
    if i < med:
        lst_sort_two.insert(0, i)
        flag += 1
    elif i == med:
        lst_sort_two.insert(flag, i)
    else:
        lst_sort_two.append(i)
        
print(f'{lst_sort_two = }')