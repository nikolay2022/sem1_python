from math import *
flag = 0
print('Введите координаты X и  Y для точки: ')
x = float(input('X='))
y = float(input('Y='))
r = float(input('R='))

if(r<0):
    print('Отрицательный радиус?')
    
if(x**2 + y**2 <= r**2) and ((x>=0 and y>=0) or (x<=0 and y<=0)): # проверка круга
     
    flag = 1

elif((x >= -r) and (y<= r) and (x<=0) and (y>=0)) or ((x>=0) and (y >= -r) and (x<=r) and (y<=0)):
    flag = 1
else:
    flag = 0
    

if flag:
    print("попадает ")
else:
    print("не попадает ")
