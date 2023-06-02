from math import *
import turtle as tr
import time

def f(x):
    y = None
    if -4 <= x <= 0:
        y = sqrt(4 - (x + 2) ** 2)
    if 0 < x <= 0.5:
        y = 0
    if 0.5 < x < 2:
        y = (log(x)) / x
    if 2 <= x <= 4:
        y = 1
    return (y)

aX = [-4, 5]
aY = [-2, 2]

Dx = 800
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
tr.setup(Dx, Dy)
Nmax = 1000
tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

tr.up()
tr.color("red")
tr.goto(-4, 0)
tr.down()
tr.goto(4, 0)
tr.up()
tr.goto(0, 0)
tr.goto(0, 3)
tr.down()
tr.goto(0, -2)
tr.up()
tr.goto(-3, 0)
for i in range(-4, 5):
    if i == 0:
        continue
    tr.goto(i, 0)
    tr.down()
    tr.goto(i, 0.25)
    tr.up()
    tr.goto(i, -0.5)
    tr.write(str(i))
    tr.up()

tr.goto(0, -9)

for i in range(-3, 3):
    tr.goto(0, i)
    tr.down()
    tr.goto(0.25, i)
    tr.up()
    tr.goto(0.5, i)
    tr.write(str(i))
    tr.up()

tr.goto(-9, 2)
x = -4
x_end = 4

tr.color("black")
step = 0.05
while (x <= x_end):
    tr.down()
    tr.goto(x, f(x))
    x += step

time.sleep(60)
