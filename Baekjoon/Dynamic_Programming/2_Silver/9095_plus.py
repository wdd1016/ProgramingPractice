import sys
input = sys.stdin.readline

t = int(input())
lst = [0 for _ in range(11)]

def numofcase(lst, num):
	if (num <= 2):
		return num
	elif (num == 3):
		return 4
	else:
		if (lst[num] != 0):
			return lst[num]
		lst[num] = numofcase(lst, num - 3) + \
			numofcase(lst, num - 2) + numofcase(lst, num - 1)
		return lst[num]
for _ in range(t):
	n = int(input())
	print(numofcase(lst, n))