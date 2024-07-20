import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
	q.append(i)

while (len(q) > 1):
	q.popleft()
	q.rotate(-1)

print(*q)