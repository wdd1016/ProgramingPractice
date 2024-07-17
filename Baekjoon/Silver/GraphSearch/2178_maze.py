import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())
field = []

for _ in range(n):
    field.append(input().rstrip())

visited = [[0] * m for _ in range(n)]

def bfs(field, visited, n, m):
    q = collections.deque()
    q.append([0, 0, 0])
    visited[0][0] == 1
    while q:
        x, y, count = q.popleft()
        count = count + 1
        if x == n - 1 and y == m - 1:
            return count
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and field[nx][ny] == '1':
                visited[nx][ny] = 1
                q.append([nx, ny, count])
    return -1

print(bfs(field, visited, n, m))