import sys, heapq

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, cost = map(int, input().rstrip().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (V + 1)
answer = 0
q = [(0, 1)]

while q:
    money, start = heapq.heappop(q)
    if not visited[start]:
        visited[start] = True
        answer += money
        for new_money, next in graph[start]:
            if not visited[next]:
                heapq.heappush(q, (new_money, next))

print(answer)
