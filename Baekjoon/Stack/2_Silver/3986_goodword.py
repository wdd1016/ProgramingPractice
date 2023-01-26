import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
count = 0
for _ in range(n):
	q = deque()
	word = input().rstrip()
	for i in range(len(word)):
		if (len(q) != 0):
			temp = q.pop()
			if (temp == word[i]):
				continue
			q.append(temp)
		q.append(word[i])
	if (len(q) == 0):
		count += 1
print(count)