#!/usr/bin/env python3
lst = []
str = raw_input('please enter:')
lst1 = str.split(' ')
for i in range(1,len(lst1)+1):
    lst.append(int(lst1.pop()))
def avge(list):
    s = 0
    for i in list:
        s += i
    avg = s/(len(list)*1.0)
    return avg
print('average is: {:.2f}'.format(avge(lst)))

