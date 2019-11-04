#!/usr/bin/env python3
with open('/tmp/String.txt') as f:
    s = f.read()
res = ""
#n = 0
for char in s:
    if char.isdigit():
        res += char
#        n += 1
print(res)
#print(n)
