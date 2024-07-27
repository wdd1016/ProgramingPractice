import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
field = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
count = []

q = deque()

for i in range(n):
    for j in range(n):
        if visited[i][j] or field[i][j] == "0":
            continue
        q.append((i, j))
        visited[i][j] = True
        count.append(1)
        while q:
            row, col = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if visited[nr][nc] == False and field[nr][nc] == "1":
                        q.append((nr, nc))
                        visited[nr][nc] = True
                        count[-1] += 1

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])
