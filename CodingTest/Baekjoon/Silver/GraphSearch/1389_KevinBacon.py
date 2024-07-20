import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    fir, sec = map(int, input().split())
    graph[fir - 1][sec - 1] = 1
    graph[sec - 1][fir - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

number = [(sum(graph[i]), i + 1) for i in range(n)]
number.sort(key = lambda x : x[0])
print(number[0][1])

# Floyd-Warshall Algorithm