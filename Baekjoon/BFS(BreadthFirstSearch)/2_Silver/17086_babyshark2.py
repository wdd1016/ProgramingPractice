from collections import deque

def maximum(arr, max, n, m):
	que = deque()
	for i in range(n):
		for j in range(m):
			if (arr[i][j] == 1):
				que.append([i, j])

	dx = [-1, -1, -1, 0, 1, 1, 1, 0] # 좌상 상 우상 우 우하 하 좌하
	dy = [-1, 0, 1, 1, 1, 0, -1, -1]

	while que:
		x, y = que.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or nx >= n or ny < 0 or ny >= m):
				continue
			if (arr[nx][ny] == 0):
				arr[nx][ny] = arr[x][y] + 1
				if (arr[nx][ny] > max):
					max = arr[nx][ny]
				que.append([nx, ny])
				continue

	return max - 1


n, m = map(int, input().split())
arr = [[0] * m for i in range(n)]
for i in range(n):
	arr[i] = list(map(int, input().split()))
print(maximum(arr, 1, n, m))