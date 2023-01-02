n = int(input())
for i in range(n):
	str1 = input()
	sum = 0
	before = 0
	for j in range(len(str1)):
		if (str1[j] == 'O'):
			before += 1
			sum += before
		else:
			before = 0
	print(sum)
