num = int(input())

for i in range(num):
	a, b, c = map(float, input().split())
	sum = a*b*c
	print("$%.2f" %(sum))