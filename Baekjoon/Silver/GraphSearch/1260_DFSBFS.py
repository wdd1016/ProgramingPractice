import sys, collections

input = sys.stdin.readline
deque = collections.deque


def dfsGraph(graph, n, visitedNodes, visitOrder, visitNode):
    visitedNodes[visitNode] = True
    visitOrder.append(visitNode)
    for i in range(1, n + 1):
        if visitedNodes[i] == False and graph[visitNode][i] == 1:
            dfsGraph(graph, n, visitedNodes, visitOrder, i)


def bfsGraph(graph, n, visitedNodes, visitOrder, firstVisitNode):
    visitedNodes[firstVisitNode] = True
    visitOrder.append(firstVisitNode)
    q = deque([firstVisitNode])
    while q:
        visitNode = q.popleft()
        for i in range(1, n + 1):
            if visitedNodes[i] == False and graph[visitNode][i] == 1:
                q.append(i)
                visitedNodes[i] = True
                visitOrder.append(i)


n, m, v = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visitedNodes = [False for _ in range(n + 1)]
visitOrder = []
dfsGraph(graph, n, visitedNodes, visitOrder, v)
print(*visitOrder)

visitedNodes = [False for _ in range(n + 1)]
visitOrder = []
bfsGraph(graph, n, visitedNodes, visitOrder, v)
print(*visitOrder)
