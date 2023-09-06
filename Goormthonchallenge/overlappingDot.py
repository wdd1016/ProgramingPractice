import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

horizon = [[0 for _ in range(n)] for _ in range(n)]
vertical = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
	ychar, xchar, d = input().split()
	y = int(ychar) - 1
	x = int(xchar) - 1

	if d == 'U' or d == 'L':
		additive = -1
	else:
		additive = 1

	if d == 'U' or d == 'D':
		while y >= 0 and y < n:
			vertical[x][y] += 1
			y += additive
	else:
		while x >= 0 and x < n:
			horizon[x][y] += 1
			x += additive

count = 0
for i in range(n):
	for j in range(n):
		if horizon[i][j] > 0 and vertical[i][j] > 0:
			count += horizon[i][j] * vertical[i][j]

print(count)