import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
islandgraph = [[] for _ in range(n+1)]

for _ in range(m):
	s, e = map(int, input().split())
	islandgraph[s].append(e)

visited = [0 for _ in range(n+1)]
unioncnt = 0
q = deque()

for i in range(1, n+1):
	if (visited[i] == 1):
		continue

	q.append(i)
	unioncnt += 1

	while (q):
		now = q.popleft()
		for to in islandgraph[now]:
			if visited[to] == 0 and now in islandgraph[to]:
				q.append(to)
				visited[to] = 1

print(unioncnt)