while True:
	a = int(input())
	if a == 0:
		break
	for i in range(1, a):
		a += i
	print(a)