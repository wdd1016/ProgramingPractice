import sys, math
input = sys.stdin.readline

strn = input().strip()
lend2 = len(strn) // 2
n = int(strn)
low = 0
high = n
while (low <= high):
	mid = (low + high) // 2
	lenmid = int(math.log10(mid)) + 1
	if (lenmid > lend2 + 1):
		high = mid
	elif (lenmid < lend2 - 1):
		low = mid
	elif (mid * mid == n):
		print(mid)
		break
	elif (mid * mid > n):
		high = mid - 1
	else:
		low = mid + 1