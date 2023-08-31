import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cnt = 0

vmap = []
for i in range(n):
	vmap += [list(map(int, input().split()))]

dx = [-1, 1, 0, 0] # 4방향
dy = [0, 0, -1, 1]
q = deque()
for i in range(n):
	for j in range(n):
		if (vmap[i][j] == 1):
			q.append([i, j])
			cnt += 1
		while (q):
			x, y = q.popleft()
			if (vmap[x][y] == 1):
				vmap[x][y] = 0
				for k in range(4):
					nx = x + dx[k]
					ny = y + dy[k]
					if (nx < 0 or nx >= n or ny < 0 or ny >= n):
						continue
					if (vmap[nx][ny] == 1):
						q.append([nx, ny])

print(cnt)

