import sys
input = sys.stdin.readline

while True:
	n = int(input())
	if (n == 0):
		break
	lst = list(str(n))
	i = 0
	k = len(lst) - 1
	while (i <= k):
		if (lst[i] != lst[k]):
			print("no")
			break
		i += 1
		k -= 1
	if (i > k):
		print("yes")