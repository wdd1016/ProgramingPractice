lst = list(map(int, input().split()))

if min(lst) == lst[2]:
	print(int(lst[0]*lst[1]/lst[2]))
elif min(lst) == lst[1]:
	print(int(lst[0]/lst[1]*lst[2]))
else:
	if max(lst) == lst[1]:
		print(int(lst[0]*lst[1]/lst[2]))
	else:
		print(int(lst[0]/lst[1]*lst[2]))