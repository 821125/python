import random
import sys
import tracemalloc
from memory_profiler import profile

# sourcery skip: for-index-underscore

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат
# и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Python 3.9.0
# OS - 64bit

@profile
def sum_series(n):
    range_number_ = 1
    sum_ = 0

    for _ in range(n):
        sum_ += range_number_
        range_number_ /= -2
    return sum_


sum_series(4)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     21     26.9 MiB     26.9 MiB           1   @profile
#     22                                         def sum_series(n):
#     23     26.9 MiB      0.0 MiB           1       range_number_ = 1
#     24     26.9 MiB      0.0 MiB           1       sum_ = 0
#     25                                         
#     26     26.9 MiB      0.0 MiB           5       for _ in range(n):
#     27     26.9 MiB      0.0 MiB           4           sum_ += range_number_
#     28     26.9 MiB      0.0 MiB           4           range_number_ /= -2
#     29     26.9 MiB      0.0 MiB           1       return sum_

# Сравним с решением через рекурсию

@profile
def rec_sum(s_n, d, n_v):
    if n_v == 0:
        return 0
    return s_n + rec_sum(s_n / d, d, n_v - 1)


rec_sum(1, -2, 4)

# Результат на единичный вызов функции
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     36     26.9 MiB     26.9 MiB           1   @profile
#     37                                         def rec_sum(s_n, d, n_v):
#     38     26.9 MiB      0.0 MiB           1       if n_v == 0:
#     39     26.9 MiB      0.0 MiB           1           return 0
#     40                                             return s_n + rec_sum(s_n / d, d, n_v - 1)

tracemalloc.start()


def sum_series(n):
    range_number_ = 1
    sum_ = 0

    for _ in range(n):
        sum_ += range_number_
        range_number_ /= -2
    return sum_


sum_series(4)

print('Current: %d, Peak %d' % tracemalloc.get_traced_memory())  # Current: 136, Peak 216

tracemalloc.start()


def rec_sum(s_n, d, n_v):
    if n_v == 0:
        return 0
    return s_n + rec_sum(s_n / d, d, n_v - 1)


rec_sum(1, -2, 4)

print('Current: %d, Peak %d' % tracemalloc.get_traced_memory())  # Current: 300, Peak 1198

print()

r = [random.randint(0, 100) for _ in range(25)]
print(f'list: {r = }\n')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'{min_index_1 = }\n{min_index_2 = }\n')
print(f'{sys.getsizeof(r) = } bytes')
print(f'{sys.getsizeof(r[0]) = } bytes')
print(f'{sys.getsizeof(tuple(r)) = } bytes')
print(f'{sys.getsizeof(tuple(r)[0]) = } bytes')

sum = 0

for size in r:
    sum += sys.getsizeof(size)
print(f'\n{sum = } bytes')

# sys.getsizeof(r) = 312 bytes
# sys.getsizeof(r[0]) = 28 bytes
# sys.getsizeof(tuple(r)) = 240 bytes
# sys.getsizeof(tuple(r)[0]) = 28 bytes

# sum = 700 bytes
