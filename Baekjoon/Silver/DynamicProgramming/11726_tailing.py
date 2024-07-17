import sys
input = sys.stdin.readline

n = int(input())

lst = [0 for _ in range(n+1)]

def findrectanc(num, lst):
	if num == 1:
		return 1
	elif num == 2:
		return 2
	elif (lst[num] == 0):
		lst[num] = (findrectanc(num - 2, lst) + \
			findrectanc(num - 1, lst)) % 10007
	return lst[num]

print(findrectanc(n, lst))