import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
prefixsum = [0 for _ in range(n)]

prefixsum[0] = lst[0]
for s in range(1, n):
	prefixsum[s] = prefixsum[s - 1] + lst[s]

for _ in range(m):
	i, j = map(int, input().split())
	sum = prefixsum[j - 1] - prefixsum[i - 1] + lst[i - 1]
	print(sum)