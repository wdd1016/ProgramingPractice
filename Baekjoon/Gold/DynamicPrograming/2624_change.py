import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
coin = []

for _ in range(k):
    coin.append(list(map(int, input().split())))

lst = [0 for _ in range(t + 1)]
lst[0] = 1

for i in range(k):
    coin_value = coin[i][0]
    coin_count = coin[i][1]
    for amount in range(t, -1, -1):
        for coin_num in range(1, coin_count + 1):
            if amount - coin_value * coin_num < 0:
                break
            else:
                lst[amount] += lst[amount - coin_value * coin_num]

print(lst[t])