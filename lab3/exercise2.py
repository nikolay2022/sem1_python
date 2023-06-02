from random import *

r = float(input("введите радиус"))
flag = 0
print(" X Y Res")
print("-------------------")
for n in range(10):
    x = uniform(-1, 4)
    y = uniform(-1, 10)

    if (x < -r) or (x > r):
        flag = 0
    if ((x >= -r) and (x <= 0) and (y >= 0)) or ((x >= 0) and (x <= r) and (y <= 0)) or (
            (x ** 2 + y ** 2 <= r ** 2) and (x > 0) and (x <= r) and (y > 0)) or (
            (x ** 2 + y ** 2 <= r ** 2) and (x < 0) and (x <= 0) and (y < 0)):
        flag = 1
    else:
        flag = 0

    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")
