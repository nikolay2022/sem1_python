from math import *
def fun(x):
    if -4<= x <= 0:
        return sqrt(4 - (x+2)**2)
    if 0 < x <= 0.5:
        return 0
    if 0.5 < x < 2 :
        return (log(x))/x
    if 2 <= x <= 4 :
        return 1
    else:
        return 'Error'
    
print(fun(float(input())))   
