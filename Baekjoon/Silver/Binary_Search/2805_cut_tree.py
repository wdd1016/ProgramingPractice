import sys, math

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort(reverse=True)
lst.append(0)

height = lst[0]
amount = 0
for i in range(n):
    difference = lst[i] - lst[i + 1]
    if difference * (i + 1) >= m - amount:
        difference = math.ceil((m - amount) / (i + 1))
        height -= difference
        break
    else:
        amount += difference * (i + 1)
        height -= difference

print(height)
