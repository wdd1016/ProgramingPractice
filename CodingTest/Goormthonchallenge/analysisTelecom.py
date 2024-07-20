import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
computerGraph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	computerGraph[a].append(b)
	computerGraph[b].append(a)

componentDensityList = []
visited = [0 for _ in range(n+1)]
q = deque()

for i in range(1, n+1):
	if visited[i] == 1:
		continue
	component = []
	count = 0
	visited[i] = 1
	q.append(i)
	while (q):
		now = q.popleft()
		component.append(now)
		for to in computerGraph[now]:
			count += 1
			if visited[to] == 0:
				q.append(to)
				visited[to] = 1
	component.sort()
	componentDensityList.append([component, count / (2 * len(component))])

componentDensityList.sort(key=lambda x: (-x[1], len(x[0]), x[0][0]))

print(*componentDensityList[0][0])