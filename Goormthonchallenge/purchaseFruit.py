import sys
input = sys.stdin.readline

n, k = map(int, input().split())

fruit = []
for i in range(n):
	fruit.append(list(map(int, input().split())))

fruit.sort(key=lambda x: x[1]/x[0], reverse=True)

fullness = 0
for i in range(n):
	if k >= fruit[i][0]:
		k -= fruit[i][0]
		fullness += fruit[i][1]
	else:
		fullness += k * (fruit[i][1]/fruit[i][0])
		k = 0
		break

print(int(fullness))