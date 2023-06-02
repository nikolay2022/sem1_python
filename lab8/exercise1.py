from math import *
def f1(a):
    y = ( (1 + pow(sin(-a),4) - pow((cos(-a)),4))/(pow(cos(a),2) ) )
    return y
def f2(a):
    y = ( 2 * tan(a)*tan(a) )
    return y
fi = open("lab1_pb_in.txt", "rt") #читатьфайл
fo = open("lab1_pb_ou.txt", "wt") #писатьвфайл
line = fi.readline() # Пропуститьстроки
line = fi.readline() # заголовкавфайле
# Вывести шапку таблицы в файл
fo.write("+======+======+=========+========+\n")
fo.write("I A I F1 I F2 I\n")
fo.write("+======+======+=========+========+\n")
for line in fi: # длявсехстрокфайла
    if line=="\n":
        continue
    b = line # расщепить
    a = float(b) # привести к вещест. типу

    # Вывод в файл
    fo.write("{0: 6.4f} I"
             .format(a))
    fo.write("{0: .2f} I"
        .format(f1(a)))
    fo.write("{0: 6.4f} I\n".format(f2(a)))
    fo.write("+------+------+---------+""--------+\n")
fi.close() # закроемфайлы
fo.close()
