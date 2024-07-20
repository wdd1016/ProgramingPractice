import sys
input = sys.stdin.readline

stra = "aeiouAEIOU"
while True:
	str1 = input()
	if str1[0] == '#':
		break
	sum = 0
	for i in range(10):
		sum += str1.count(stra[i])
	print(sum)