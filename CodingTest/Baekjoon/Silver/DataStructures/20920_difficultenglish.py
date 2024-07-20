import sys
input = sys.stdin.readline

n, m = map(int, input().split())

from collections import defaultdict

cadet = defaultdict(int)
for i in range(n):
	w  = input().strip()
	if (len(w) >= m):
		cadet[w] += 1

lst = sorted(list(cadet.items()), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in range(len(lst)):
	print(lst[i][0])