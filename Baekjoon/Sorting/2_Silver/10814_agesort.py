import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	temp = list(input().split())
	temp[0] = int(temp[0])
	lst += [temp]
lst.sort(key=lambda x: x[0])
for i in range(n):
	print(*lst[i])