#!/usr/bin/env python3
def change():
    a = 90
    print(a)
a = 9
print(a)
change()
print(a)


def changeglobal():
    global a
    print(a)
    a = 900
    print(a)
print(a)
changeglobal()
print(a)
