import sys

input = sys.stdin.readline

node = int(input())
edge = int(input())

graph = [[0] * (node + 1) for _ in range(node + 1)]

for _ in range(edge):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

infected = [0 for _ in range(node + 1)]


def virus(point):
    if infected[point] == 1:
        return
    infected[point] = 1
    for i in range(1, node + 1):
        if graph[point][i] == 1:
            virus(i)


virus(1)
print(sum(infected) - 1)
