import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(nodeNum, adj_list, visited):
    visited[nodeNum] = True
    for node in adj_list[nodeNum]:
        if visited[node] == False:
            dfs(node, adj_list, visited)


n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
visited = [False] * n
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u - 1].append(v - 1)
    adj_list[v - 1].append(u - 1)

for i in range(n):
    if visited[i] == False:
        dfs(i, adj_list, visited)
        count += 1

print(count)
