#!/usr/bin/env python3
principal = float(input('please enter benjin:'))
inrate = float(input('please enter lilv:'))
item = int(input('please enter nianxian:'))
sum = 0
for i in range(1,item+1):
    sum = principal + principal*inrate
    print('year{} total is {:.2f}'.format(i,sum))
    principal = sum
#year = 1
#while year <= item:
 #   sum = principal + principal*inrate
  #  print('year{} total is {:.2f}'.format(year,sum))
   # principal = sum
    #year = year + 1
