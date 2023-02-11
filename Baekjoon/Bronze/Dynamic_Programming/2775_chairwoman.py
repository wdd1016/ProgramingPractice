import sys
input = sys.stdin.readline

def lstpeople(floor, unit, lst):
	for f in range(floor + 1):
		addlst = []
		for u in range(unit):
			if (f == 0):
				addlst.append(u+1)
			else:
				if (u == 0):
					addlst.append(1)
				else:
					addlst.append(lst[f-1][u] + addlst[u-1])
		lst.append(addlst)

t = int(input())
for _ in range(t):
	k = int(input())
	n = int(input())
	lst = []
	lstpeople(k, n, lst)
	print(lst[k][n-1])
