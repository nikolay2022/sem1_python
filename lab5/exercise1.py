some_str = input()
some_str += ' '
words = list()
symbols = ' _.,;:\n\t!?'
arifms = '+-=*'
word = ''
count = 0
flag = False

for letter in some_str:

    if letter not in symbols:
        word += letter
    else:
        words.append(word)
        word = ''

for i in words:
    flag = False
    if i[0].isupper():
        for o in i:
            if o in arifms:
                count = count + 1
    for m in range(1,len(i)):
        if i[m] == i[m-1]:
            flag = True
    if flag:
        print(i)

print(count)
