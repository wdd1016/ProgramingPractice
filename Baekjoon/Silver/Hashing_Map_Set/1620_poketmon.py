import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict1 = {}
for i in range(1, n+1):
	str1 = input().strip()
	strint = str(i)
	dict1[strint] = str1
	dict1[str1] = strint

for _ in range(m):
	print(dict1[input().strip()])