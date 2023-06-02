from math import *

def fun(x):
    if -4 <= x <= 0:
        return sqrt(4 - (x + 2) ** 2)
    if 0 < x <= 0.5:
        return 0
    if 0.5 < x < 2:
        return (log(x)) / x
    if 2 <= x <= 4:
        return 1
    else:
        return None

print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I X I Y I")
print("+--------+--------+")

while xt <= xe:
    y = fun(xt)
    print(xt, y)
    xt += dx
print("+--------+--------+")
