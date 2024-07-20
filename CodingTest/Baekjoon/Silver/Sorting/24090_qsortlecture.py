import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def partition(lst, start, end, count):
	x = lst[end]
	i = start - 1
	for j in range(start, end):
		if (lst[j] <= x):
			i += 1
			count[0] += 1
			if (count[0] == k):
				print(min(lst[i], lst[j]), max(lst[i], lst[j]))
				exit(0)
			lst[i], lst[j] = lst[j], lst[i]
	if (i+1 != end):
		count[0] += 1
		if (count[0] == k):
			print(min(lst[i+1], lst[end]), max(lst[i+1], lst[end]))
			exit(0)
		lst[i+1], lst[end] = lst[end], lst[i+1]
	return i + 1

def qsort(lst, start, end, count):
	if (start < end):
		mid = partition(lst, start, end, count)
		qsort(lst, start, mid - 1, count)
		qsort(lst, mid + 1, end, count)

n, k = map(int, input().split())
lst = list(map(int, input().split()))
count = [0, k]
qsort(lst, 0, n-1, count)
if (count[0] < count[1]):
	print(-1)