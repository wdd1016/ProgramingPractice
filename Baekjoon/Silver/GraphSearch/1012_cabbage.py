import sys
from collections import deque
input = sys.stdin.readline

def count_bugs(m, n, lst):
	count = 0
	dx = [-1, 1, 0, 0] # 4방향
	dy = [0, 0, -1, 1]
	q = deque()
	for i in range(m):
		for j in range(n):
			if (lst[i][j] == 1):
				q.append([i, j])
				count += 1
			while (q):
				x, y = q.popleft()
				if (lst[x][y] == 1):
					lst[x][y] = 0
					for k in range(4):
						nx = x + dx[k]
						ny = y + dy[k]
						if (nx < 0 or nx >= m or ny < 0 or ny >= n):
							continue
						if (lst[nx][ny] == 1):
							q.append([nx, ny])
	return count


t = int(input())
for i in range(t):
	m, n, k = map(int, input().split())
	lst = [[0 for _ in range(n)] for _ in range(m)]
	for j in range(k):
		x, y = map(int, input().split())
		lst[x][y] = 1
	print(count_bugs(m, n, lst))