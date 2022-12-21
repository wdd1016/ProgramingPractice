lst = list(map(int, input().split()))

for i in range(8):
	if (lst[i] < 0 or lst[i] > 1):
		print("F")
		break
	if (i == 7):
		print("S")
		break