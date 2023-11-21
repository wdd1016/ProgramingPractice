import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
p = []
n = []

for _ in range(k):
    amount, count = map(int, input().split())
    p.append(amount)
    n.append(count)

lst = [0 for _ in range(10001)]

# def find_exchange_count(money, lst):
# 	if lst[money] == 0:
# 		for i in range(k):
# 			temp = find_exchange_count(money - p[i], lst)
# 			if
