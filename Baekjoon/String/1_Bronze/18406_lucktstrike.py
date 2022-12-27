n = str(input())
l = len(n)
sum1 = 0
sum2 = 0

if (l % 2 != 0):
	print("READY")

else:
	for i in range(l//2):
		sum1 += int(n[i])
		sum2 += int(n[l - 1 - i])
	if (sum1 == sum2):
		print("LUCKY")
	else:
		print("READY")
