import sys
input = sys.stdin.readline

for _ in range(3):
	lst = list(map(int, input().split()))
	level = "EABCD"
	print(level[lst.count(0)])