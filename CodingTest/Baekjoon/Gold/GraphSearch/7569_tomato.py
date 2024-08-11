from collections import deque
import sys

input = sys.stdin.readline


def checkAllRipe(tomatoes, totalDays, m, n, h):
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 0:
                    return -1
    return totalDays


tomatoes = []
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def BFS(tomatoes, direction):
    m, n, h = map(int, input().split())

    for i in range(h):
        tomatoes.append([])
        for _ in range(n):
            tomatoes[i].append(list(map(int, input().split())))

    answer = 0
    q = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == 1:
                    q.append([z, y, x, 0])

    while q:
        z, y, x, day = q.popleft()
        if day > answer:
            answer = day
        for dz, dy, dx in direction:
            nz = z + dz
            ny = y + dy
            nx = x + dx
            if (
                0 <= nx < m
                and 0 <= ny < n
                and 0 <= nz < h
                and tomatoes[nz][ny][nx] == 0
            ):
                tomatoes[nz][ny][nx] = 1
                q.append([nz, ny, nx, day + 1])

    print(checkAllRipe(tomatoes, answer, m, n, h))


BFS(tomatoes, direction)
