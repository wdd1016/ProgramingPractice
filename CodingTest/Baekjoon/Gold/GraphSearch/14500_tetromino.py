import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# direction
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

maximum = 0


def dfs(r, c, total, count):
    global maximum
    if count == 4:
        maximum = max(maximum, total)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        dfs(nr, nc, total + graph[nr][nc], count + 1)
        visited[nr][nc] = False


def findT(r, c):
    global maximum
    neighborhood = []
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        neighborhood.append(graph[nr][nc])
    if len(neighborhood) == 4:
        neighborhood.remove(min(neighborhood))
    if len(neighborhood) == 3:
        maximum = max(maximum, sum(neighborhood) + graph[r][c])


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        findT(i, j)
        visited[i][j] = False

print(maximum)
