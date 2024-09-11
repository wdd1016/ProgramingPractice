import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

picture = [list(input().rstrip()) for _ in range(n)]
normal_visited = [[False for _ in range(n)] for _ in range(n)]
normal_count = 0

for row in range(n):
    for col in range(n):
        if normal_visited[row][col] == True:
            continue
        q = deque()
        q.append((picture[row][col], row, col))
        normal_visited[row][col] = True
        normal_count += 1
        while q:
            color, r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and picture[nr][nc] == color
                    and normal_visited[nr][nc] == False
                ):
                    normal_visited[nr][nc] = True
                    q.append((picture[nr][nc], nr, nc))

blind_visited = [[False for _ in range(n)] for _ in range(n)]
blind_count = 0

for row in range(n):
    for col in range(n):
        if blind_visited[row][col] == True:
            continue
        q = deque()
        q.append((picture[row][col], row, col))
        blind_visited[row][col] = True
        blind_count += 1
        while q:
            color, r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and blind_visited[nr][nc] == False:
                    if (color == "B" and picture[nr][nc] == "B") or (
                        color != "B" and picture[nr][nc] != "B"
                    ):
                        blind_visited[nr][nc] = True
                        q.append((picture[nr][nc], nr, nc))

print(normal_count, blind_count)
