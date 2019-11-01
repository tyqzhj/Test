#!/usr/bin/env python3
n = int(input('Enter the value of n:'))
print('Enter values of the Matrix A:')
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print('Enter values of the Matrix B:')
b = []
for i in range(n):
    b.append([int(y) for y in input().split()])
print('matrix multiplication:')
c = []
for x in range(n):
    c.append([a[i][j]*b[i][j] for j in range(n)])
for x in c:
    for y in x:
        print(str(y).rjust(5),end=' ')
    print()
