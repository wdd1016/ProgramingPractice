remain = 1000 - int(input())
lst = [500, 100, 50, 10, 5, 1]
count = 0

for i in range(6):
	count += remain // lst[i]
	remain %= lst[i]

print(count)