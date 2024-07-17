from collections import deque
import sys

input = sys.stdin.readline


def bfsForTomato(tomatoMap, q):
    leastDay = 0
    while q:
        x, y, day = q.popleft()
        leastDay = day if day > leastDay else leastDay
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif tomatoMap[ny][nx] == 0:
                tomatoMap[ny][nx] = 1
                q.append([nx, ny, day + 1])
    for y in range(n):
        for x in range(m):
            if tomatoMap[y][x] == 0:
                return -1
    return leastDay


m, n = map(int, input().split())

tomatoMap = []
q = deque()

for y in range(n):
    tomatoMap.append(list(map(int, input().split())))
    for x in range(m):
        if tomatoMap[y][x] == 1:
            q.append([x, y, 0])

print(bfsForTomato(tomatoMap, q))
