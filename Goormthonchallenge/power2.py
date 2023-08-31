import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = [0 for i in range(32)]

vmap = []
for i in range(n):
	vmap += [list(map(int, input().split()))]

dx = [-1, 1, 0, 0] # 4방향
dy = [0, 0, -1, 1]
q = deque()
for i in range(n):
	for j in range(n):
		mrc = vmap[i][j]
		vilcnt = 0
		if (mrc != 0):
			q.append([i, j])
		while (q):
			x, y = q.popleft()
			if (vmap[x][y] == mrc):
				vmap[x][y] = 0
				vilcnt += 1
				for m in range(4):
					nx = x + dx[m]
					ny = y + dy[m]
					if (nx < 0 or nx >= n or ny < 0 or ny >= n):
						continue
					if (vmap[nx][ny] == mrc):
						q.append([nx, ny])
		if (vilcnt >= k):
			cnt[mrc] += 1
maxcnt = max(cnt)
for i in range(n, -1, -1):
	if (cnt[i] == maxcnt):
		print(i)
		break
