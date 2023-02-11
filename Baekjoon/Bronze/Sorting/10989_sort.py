import sys
input = sys.stdin.readline

n = int(input())
lst = [0 for _ in range(10001)]
for i in range(n):
	lst[int(input())] += 1
for i in range(1, 10001):
	for j in range(lst[i]):
		print(i)