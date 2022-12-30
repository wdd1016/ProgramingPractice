n = int(input())
menu = [0 for _ in range(2*n)]
menu = list(map(int, input().split()))
sticker = [0 for _ in range(n+1)]
current = 0
max = 0

for i in range(2*n):
	if (sticker[menu[i]] == 0):
		sticker[menu[i]] = 1
		current += 1
		if (current > max):
			max = current
	else:
		sticker[menu[i]] = 0
		current -= 1

print(max)