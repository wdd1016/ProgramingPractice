import sys, re
from functools import cmp_to_key

input = sys.stdin.readline


def ruleForSerial(x, y):
    if len(x) != len(y):
        if len(x) > len(y):
            return 1
        else:
            return -1
    else:
        a = re.findall(r"\d", x)
        b = re.findall(r"\d", y)
        a = sum(list(map(int, a)))
        b = sum(list(map(int, b)))
        if a == b:
            if x > y:
                return 1
            if x == y:
                return 0
            else:
                return -1
        else:
            if a > b:
                return 1
            else:
                return -1


n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())

lst.sort(key=cmp_to_key(ruleForSerial))

for i in range(n):
    print(lst[i])
