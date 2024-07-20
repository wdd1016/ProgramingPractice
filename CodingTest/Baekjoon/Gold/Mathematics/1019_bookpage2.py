import sys, math
input = sys.stdin.readline

num = int(input())
lst = [0 for _ in range(10)]
n = num
after = 1

while n > 0:
	standard = n % 10
	n = n // 10
	for i in range(10):
		if (i == 0):
			if (standard == 0):
				lst[i] += (n - 1) * after + (num % after + 1)
			else:
				lst[i] += n * after
		elif (i < standard):
			lst[i] += (n + 1) * after
		elif (i == standard):
			lst[i] += n * after + (num % after + 1) # ex) 21233 1측정시 0~233 234개
		else:
			lst[i] += n * after
	after *= 10

print(*lst)