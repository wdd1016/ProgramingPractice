c = int(input())

for _ in range(c):
	lst = list(map(int, input().split()))
	n = lst.pop(0)
	average = sum(lst) / n
	count = 0
	for i in range(n):
		if (lst[i] > average):
			count += 1
	ans = round(100 * count / n, 3)
	print("{:.3f}%".format(ans)) 