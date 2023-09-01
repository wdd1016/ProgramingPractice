import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

connection = [[] for _ in range(n + 1)]
for i in range(m):
	a, b = map(int, input().split())
	connection[a].append(b)
	connection[b].append(a)

for i in range(n + 1):
	connection[i].sort()

visit = [False for _ in range(n + 1)]
pos = k

while True:
	if visit[pos] == True:
		break
	else:
		visit[pos] = True
		if len(connection[pos]) == 0:
			break
		else:
			for i in range(len(connection[pos])):
				if visit[connection[pos][i]] == False:
					pos = connection[pos][i]
					break

print(visit.count(True), pos)