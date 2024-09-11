import sys

input = sys.stdin.readline

m, n = map(int, input().split())

snacks = list(map(int, input().split()))

answer = 0
low = 1
high = 1000000000
while low <= high:
    mid = (low + high) // 2
    count = 0
    for snack in snacks:
        count += snack // mid
    if count >= m:
        answer = max(answer, mid)
        low = mid + 1
    else:
        high = mid - 1

print(answer)
