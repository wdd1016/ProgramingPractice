import math
k, n = map(int, input().split())

if n <= 1:
	print(-1)
else:
	print(k + math.ceil(k / (n - 1)))