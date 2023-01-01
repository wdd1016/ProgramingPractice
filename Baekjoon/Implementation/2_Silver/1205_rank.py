import sys
input = sys.stdin.readline

n, nscore, p = map(int, input().split())
if n == 0: # p는 10이상이므로 항상 1 출력
	print(1)
else:
	lst = list(map(int, input().split()))

firindex = -1
for i in range(n):
	if (lst[i] < nscore):
		if (firindex != -1):
			print (firindex + 1)
		else:
			print(i+1)
		break
	elif (lst[i] == nscore):
		if (firindex == -1):
			firindex = i
		if (i == n-1):
			if (n < p):
				print(firindex + 1)
			else:
				print(-1)
	else:
		if (i == n-1):
			if (n < p):
				print(n + 1)
			else:
				print(-1)