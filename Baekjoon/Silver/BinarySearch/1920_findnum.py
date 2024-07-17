import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))
lst.sort()

def binary_search(key, low, high):
	while (low <= high):
		mid = (low + high) // 2
		if (lst[mid] == key):
			print(1)
			break
		elif (lst[mid] > key):
			high = mid - 1
		else:
			low = mid + 1
	if (low > high):
		print(0)

for i in range(m):
	binary_search(mlst[i], 0, n-1)