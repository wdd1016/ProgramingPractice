import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [list(input().split()) for i in range(n)]
ans = [[0] * n for i in range(n)]

for i in range(k):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	for newy in range(y - 1, y + 2):
		if (newy < 0) or (newy >= n):
			continue
		if (newy == y):
			for newx in range(x - 1, x + 2):
				if (newx < 0) or (newx >= n):
					continue
				if arr[newy][newx] == '0':
					ans[newy][newx] += 1
				elif arr[newy][newx] == '@':
					ans[newy][newx] += 2
		else:
			if arr[newy][x] == '0':
				ans[newy][x] += 1
			elif arr[newy][x] == '@':
				ans[newy][x] += 2

max = 0
for i in range(n):
    for j in range(n):
        if ans[i][j] > max:
            max = ans[i][j]

print(max)