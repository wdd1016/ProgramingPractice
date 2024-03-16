import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

idx = [i for i in range(n)]

idx.sort(key=lambda x: lst[x])

count = -1
lastValue = -(10**9) - 1

for i in idx:
    if lst[i] == lastValue:
        lst[i] = count
    else:
        count += 1
        lastValue = lst[i]
        lst[i] = count

print(*lst)
