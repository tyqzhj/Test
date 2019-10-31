#!/usr/bin/env python3
def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b
    print()
n = int(input())
print(fib(n))
