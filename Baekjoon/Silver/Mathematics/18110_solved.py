import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    exceptionNum = int(n * 0.15 + 0.5)
    if exceptionNum == 0:
        print(int(sum(lst) / n + 0.5))
    else:
        print(int(sum(lst[exceptionNum:-exceptionNum]) / (n - 2 * exceptionNum) + 0.5))
