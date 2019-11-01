#!/usr/bin/env python3
n = int(input('Enter the number of students:'))
data = {}
Subjects = ('physics','math','history')
for i in range(1,n+1):
    name = input('please Enter student {}:'.format(i))
    marks = []
    for x in Subjects:
        marks.append(int(input('please enter marks of {}:'.format(x))))
    data[name] = marks
print(data)
for x,y in data.items():
    total = sum(y)
    if total < 120:
        print('{} failed'.format(x))
    else:
        print('{} passed'.format(x))
