import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
now = 0
lst2 = []

for i in range(n):
	now -= 1
	now = now + k
	if (now >= len(lst)):
		while (now >= len(lst)):
			now -= len(lst)
	lst2.append(lst.pop(now))

print("<", end="")
print(', '.join(map(str, lst2)), end="")
print(">")