import sys

input = sys.stdin.readline

n = int(input())

minimal = [-1 for _ in range(n + 1)]
minimal[1] = 0

last = [0 for _ in range(n + 1)]

stack = [n]

while stack:
    num = stack[-1]
    if minimal[num] != -1:
        stack.pop()
        continue
    if num % 3 == 0 and num % 2 == 0:
        lst = [num // 3, num // 2, num - 1]
    elif num % 3 == 0:
        lst = [num // 3, num - 1]
    elif num % 2 == 0:
        lst = [num // 2, num - 1]
    else:
        lst = [num - 1]
    minCnt = n
    minValue = n
    for i in lst:
        if minimal[i] == -1:
            stack.append(i)
            minCnt = 0
        elif minCnt != 0 and minimal[i] < minCnt:
            minCnt = minimal[i]
            minValue = i
    if stack[-1] == num:
        minimal[num] = minCnt + 1
        last[num] = minValue
        stack.pop()

print(minimal[n])

while n != 1:
    print(n, end=" ")
    n = last[n]

print(n)
