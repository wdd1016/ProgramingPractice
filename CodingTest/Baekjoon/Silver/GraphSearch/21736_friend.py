import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
x, y = 0, 0

for i in range(n):
    campus.append(input().rstrip())
    if campus[i].find("I") != -1:
        x = i
        y = campus[i].find("I")
count = 0


def dfsCampus(campus, x, y):
    global count
    global n
    global m

    if campus[x][y] == "X":
        return
    elif campus[x][y] == "P":
        count += 1

    campus[x] = campus[x][:y] + "X" + campus[x][y + 1 :]
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        dfsCampus(campus, nx, ny)


dfsCampus(campus, x, y)
if count == 0:
    print("TT")
else:
    print(count)
