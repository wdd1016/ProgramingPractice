import sys

input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

result = []
for i in range(n):
    rank = 1
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank = rank + 1
    result.append(rank)

print(*result)
