import cProfile
import math
import timeit


# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Для примера возьмем следующую задачу:
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def sum_series(n):
    range_number_ = 1
    sum_ = 0

    for _ in range(n):  # O(n)
        sum_ += range_number_
        range_number_ /= -2
    return sum_
# сложность алгоритма равна O(n)


sum_series(4)


# Сравним с решением через рекурсию
def rec_sum(s_n, d, n_v):
    if n_v == 0:
        return 0
    return s_n + rec_sum(s_n / d, d, n_v - 1)


rec_sum(1, -2, 4)


def main():
    sum_series(400)
    rec_sum(1, -2, 400)


cProfile.run('main()')               # 406 function calls (6 primitive calls) in 0.001 seconds
cProfile.run('sum_series(400)')      # 004 function calls in 0.000 seconds
cProfile.run('rec_sum(1, -2, 400)')  # 404 function calls (4 primitive calls) in 0.000 seconds


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
def find_primes(i):
    count1_, count2_ = 1, 0
    while count2_ < i:
        count1_ += 1
        if (math.factorial(count1_ - 1) + 1) % count1_ == 0:
            count2_ += 1
    return count1_


# Согласно функции распределения простых чисел,
# количество простых чисел на отрезке [1;n] растёт с увеличением n как n / ln(n)
def find_range(i):
    range_ = 0
    number = 2
    while range_ <= i:  # сложность while loop = O(n)
        range_ = number / math.log(number)
        number += 1
    return number
# сложность алгоритма равна O(n)


# Ищем i-е простое число используя алгоритм «Решето Эратосфена»
def find_primes_e(i):
    lst_prime = [_ for _ in range(2, find_range(i))]

    for number in lst_prime:  # O(n)
        if lst_prime.index(number) > number - 1:
            break
        for j in range(2, len(lst_prime)):  # O(n)
            if number * j in lst_prime[number:]:
                lst_prime.remove(number * j)
    return lst_prime[i - 1]
# сложность алгоритма равна O(n) * O(n) = O(n ** 2)
# увеличение количества чисел в 10 раз увеличивает время выполнения приблизительно в 100 раз


print(f'{find_primes(3) = }')
print(f'{find_primes_e(3) = }')
print()

number_executions = 5
test_value = 15

time1 = timeit.timeit(f'find_range({test_value})',
                      setup='from __main__ import find_range',
                      number=number_executions)
# function find_range time result = 0.0001224999999999976

time2 = timeit.timeit(f'find_primes_e({test_value})',
                      setup='from __main__ import find_primes_e',
                      number=number_executions)
# function find_primes_e time result = 0.0009507000000000057

print(f'function find_range time result = {time1}\nfunction find_primes_e time result = {time2}\n')

cProfile.run('find_range(1000)')     # 09122 function calls in 0.005 seconds
cProfile.run('find_primes_e(1000)')  # 19372 function calls in 4.776 seconds
