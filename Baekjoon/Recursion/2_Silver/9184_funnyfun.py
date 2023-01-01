import sys

def funny(a, b, c, lst):
	if (a <= 0 or b <= 0 or c <= 0):
		return 1
	if (a > 20 or b > 20 or c > 20):
		return 1048576
	if (lst[a][b][c] != 0):
		return lst[a][b][c]
	elif (a < b and b < c):
		lst[a][b][c] = (funny(a, b, c-1, lst) + 
		funny(a, b-1, c-1, lst) - funny(a, b-1, c, lst))
		return lst[a][b][c]
	else:
		lst[a][b][c] = (funny(a-1, b, c, lst) +
		funny(a-1, b-1, c, lst) + funny(a-1, b, c-1, lst) - funny(a-1, b-1, c-1, lst))
		return lst[a][b][c]

lst = [[[0]*21 for _ in range(21)] for _ in range(21)]
while True:
	a, b, c = map(int, sys.stdin.readline().split())
	if (a == -1 and b == -1 and c == -1):
		break
	else:
		print("w(%d, %d, %d) = %d" % (a, b, c, funny(a, b, c, lst)))