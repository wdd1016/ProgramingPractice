import sys

input = sys.stdin.readline

a = 0
for i in range(10):
    if i % 2 == 0:
        pass
        a = a + 2
    elif i % 5 == 0:
        break
        a = a + 5
    else:
        continue
        a = a + 1

print(a)
