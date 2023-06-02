from random import random

import numpy as np

n = int(input("Введите размер матрицы (NxN): "))
# Матрица со случайным набором значений
A = 20 * np.random.random(size=(n, n)) - 10

for Row in range(n):
    for Col in range(n):
        print("{0:>5.2f}".format(A[Row][Col]), end=" ")
    print()
print()

for x in range(n):
    summ = 0
    for y in range(n):
        if A[x][y] >= 0:
            summ = summ + A[x][y]
        else:
            summ = 0
            break
    print("сумма в", x, "строчке:", summ)

min_sum = A[0][0]

for i in range(n):
    t1 = 0
    t2 = 0
    for j in range(n-i):
        t1 += A[i+j][j]
        t2 += A[j][i+j]
    if t1 < min_sum: min_sum = t1
    if t2 < min_sum: min_sum = t2

print(A)
print(min_sum)
