import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0 for _ in range(n + 1)]]

for _ in range(n):
    graph.append([0])
    graph[-1].extend(map(int, input().split()))

ps_graph = [[0 for _ in range(n + 1)]]
for i in range(1, n + 1):
    ps_graph.append([0])
    for j in range(1, n + 1):
        b_sum = ps_graph[i - 1][j] + ps_graph[i][j - 1] - ps_graph[i - 1][j - 1]
        ps_graph[-1].append(b_sum + graph[i][j])

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total_sum = ps_graph[x2][y2]
    north_out_sum = ps_graph[x1 - 1][y2]
    west_out_sum = ps_graph[x2][y1 - 1]
    diagonal_out_sum = ps_graph[x1 - 1][y1 - 1]
    print(total_sum - north_out_sum - west_out_sum + diagonal_out_sum)
