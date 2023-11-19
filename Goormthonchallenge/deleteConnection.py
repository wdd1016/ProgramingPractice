def f(i, j, c):
	arr[i][j] = c
	stack = [(i, j)]
	visited = set()
	
	while stack:
		y, x = stack.pop()
		
		if (y, x) in visited:
			continue
		
		visited.add((y, x))
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != arr[y][x]:
				continue
			
			stack.append((ny, nx))
	
	if len(visited) >= K:
		for y, x in visited:
			arr[y][x] = "."

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, K, Q = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for _ in range(Q):
	i, j, c = input().split()
	f(int(i) - 1, int(j) - 1, c)

for i in arr:
	print(''.join(i))