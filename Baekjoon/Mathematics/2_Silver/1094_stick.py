import sys
input = sys.stdin.readline

x = int(input())
lst = [64]

while True:
	idx = lst.index(min(lst))
	if (sum(lst) == x):
		print(len(lst))
		break
	lst[idx] = lst[idx] // 2
	if sum(lst) > x:
		continue
	elif sum(lst) == x:
		print(len(lst))
		break
	else:
		lst.append(lst[idx])