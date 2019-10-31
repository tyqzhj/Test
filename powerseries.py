#!/usr/bin/env python3
x = float(input('enter the value of x:'))
result = 1.0
temp = 1
i = 1
while i < 100:
    temp = temp*x/i
    result = result + temp
    i += 1
    if temp < 0.0001:
        break
print('Times={} and Sum={}'.format(i,result))
