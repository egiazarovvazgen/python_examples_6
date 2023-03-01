"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(то есть не меньше заданного минимума и не больше заданного максимума).
"""

import random
size = int(input("Введите размер списка: "))
lstFirst = [random.randint(-10, 10) for _ in range(size)]
print(lstFirst)
minNumber = int(input("Введите минимум: "))
maxNumber = int(input("Введите максимум: "))
lstSecond = []
for i in range(len(lstFirst)):
    if minNumber <= lstFirst[i] <= maxNumber:
        lstSecond.append(i)
print(f"Индексы элементов массива (списка), значения которых принадлежат заданному диапазону: {lstSecond}")
