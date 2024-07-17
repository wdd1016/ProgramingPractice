from collections import deque
import sys
input = sys.stdin.readline

def area(que, lst):
	defarea = 0
	dx = [-1, 1, 0, 0] # 상 하 좌 우
	dy = [0, 0, -1, 1]
	while que:
		x, y = que.popleft()
		if (lst[x][y] == 1):
			lst[x][y] = 0
			defarea += 1
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if (nx < 0 or nx >= n or ny < 0 or ny >= m):
					continue
				if (lst[nx][ny] == 1):
					que.append([nx, ny])
	return defarea

n, m = map(int, input().split())
lst = []
que = deque()
count = 0
max = 0

for i in range(n):
	lst.append(list(map(int, input().split())))

for i in range(n):
	for j in range(m):
		if (lst[i][j] == 1):
			count += 1
			que.append([i, j])
			now_area = area(que, lst)
			if (now_area > max):
				max = now_area

print(count)
print(max)