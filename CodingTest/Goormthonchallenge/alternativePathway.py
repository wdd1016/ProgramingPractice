import sys
from collections import deque
input = sys.stdin.readline

n, m, s, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

q = deque()

for i in range(1, n+1):
	path = [-2 for _ in range(n+1)]
	path[s] = 0
	q.append(s)
	while (q):
		curr = q.popleft()
		for next in graph[curr]:
			if path[next] == -2 and curr != i and next != i:
				path[next] = path[curr] + 1
				if (next == e):
					q.clear()
				q.append(next)
	print(path[e] + 1)

	