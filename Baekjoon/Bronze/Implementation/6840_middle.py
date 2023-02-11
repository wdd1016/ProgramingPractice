a = int(input())
b = int(input())
c = int(input())

min3 = min(a, b, c)
max3 = max(a, b, c)
if (a != min3 and a != max3):
	print(a)
if (b != min3 and b != max3):
	print(b)
if (c != min3 and c != max3):
	print(c)