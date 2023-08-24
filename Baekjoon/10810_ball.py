import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for s in range(i - 1, j):
        lst[s] = k
print(*lst)