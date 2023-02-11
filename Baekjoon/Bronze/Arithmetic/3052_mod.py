count = [0 for _ in range(42)]
count_int = 0

for _ in range(10):
	count[int(input()) % 42] += 1

for i in range(42):
	if count[i] > 0 : count_int += 1

print(count_int)