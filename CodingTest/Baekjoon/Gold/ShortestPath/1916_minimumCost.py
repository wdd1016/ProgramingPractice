import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [sys.maxsize] * (n + 1)  # 시작 노드에서부터 해당 노드로 가는 최소 비용
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]  # node1에서 [node2, node2로 가는 비용]

for _ in range(m):
    node1, node2, cost = map(int, input().split())
    graph[node1].append([node2, cost])

start, end = map(int, input().split())

# Dijkstra Algorithm
q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dis, node = heapq.heappop(q)
    if dis > distance[node]:  # 이미 저장된 최소비용이 현재값보다 작다면
        continue

    for lst in graph[node]:
        newCost = lst[1] + distance[node]  # node2로 가는 비용 + 현재까지의 최소 비용

        # newCost가 기존 node2까지의 최소비용보다 작다면
        if newCost < distance[lst[0]]:
            distance[lst[0]] = newCost
            heapq.heappush(q, (newCost, lst[0]))

print(distance[end])
