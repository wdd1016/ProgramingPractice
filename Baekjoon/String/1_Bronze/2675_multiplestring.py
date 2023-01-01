import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	temp, lst = input().strip().split()
	r = int(temp)
	for i in range(len(lst)):
		for j in range(r):
			print(lst[i], end="")
	print("")