import sys
input = sys.stdin.readline
from collections import deque

n, k, q = map(int, input().split())

stringbox = []
for _ in range(n):
	stringbox.append(list(input().strip()))

for _ in range(q):
	y, x, d = map(int, input().split())
	stringbox[y-1][x-1] = d
	dq = deque()
	dq.append((y-1, x-1))
	cnt = 0
	while dq:
		ny, nx = dq.popleft()
		if ny >= 0 and nx >= 0 and ny < n and nx < n and stringbox[ny][nx] == d:
			cnt += 1
			
