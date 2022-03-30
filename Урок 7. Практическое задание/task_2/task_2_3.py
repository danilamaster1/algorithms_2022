"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from timeit import timeit
from statistics import median
from random import randint

m = int(input("Введите m: "))
lst_obj = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: \n{lst_obj}\n')
print(f'Медиана - {median(lst_obj[:])}')


print(timeit("median(lst_obj[:])", globals=globals(), number=1000))

"""
m = 10
0.0006964999993215315

m = 100
0.007622099999935017

m = 1000
0.17955049999909534
"""
