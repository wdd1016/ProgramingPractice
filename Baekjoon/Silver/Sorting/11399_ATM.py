import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort(reverse=True)

answer = 0

for i in range(n):
    answer += (i + 1) * lst[i]

print(answer)
