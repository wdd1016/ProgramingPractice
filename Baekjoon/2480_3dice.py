lst = list(map(int, input().split()))

while True:
	for i in range(1,7):
		if lst.count(i) == 3:
			print(10000 + i * 1000)
			break;
	for i in range(1,7):
		if lst.count(i) == 2:
			print(1000 + i * 100)
			break;
	for i in range(6,0):
		if lst.count(i) == 1:
			print(i * 100)
			break;