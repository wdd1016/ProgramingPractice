import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

n, m = map(int, input().split())

answer = [[0 for _ in range(m)] for _ in range(n)]
ground = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if 2 in ground[i]:
        goal = [i, ground[i].index(2), 0]

q = deque()
q.append(goal)

while q:
    now = q.popleft()
    if answer[now[0]][now[1]] == 0:
        answer[now[0]][now[1]] = now[2]
    else:
        continue
    for i in range(4):
        nr = now[0] + dr[i]
        nc = now[1] + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or ground[nr][nc] != 1:
            continue
        q.append([nr, nc, now[2] + 1])

for i in range(n):
    for j in range(m):
        if answer[i][j] == 0 and ground[i][j] == 1:
            answer[i][j] = -1
    print(*answer[i])
