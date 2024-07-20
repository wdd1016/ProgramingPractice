import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sset = set()
count = 0

for _ in range(n):
    sset.add(input().rstrip())

for _ in range(m):
    if input().rstrip() in sset:
        count += 1

print(count)
