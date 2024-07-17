import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	lst.append(input().strip())

lst.sort()
print(max(lst, key=lst.count))