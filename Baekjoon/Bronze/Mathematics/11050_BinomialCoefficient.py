import sys

input = sys.stdin.readline

n, k = map(int, input().split())

numerator = 1
for i in range(n - k + 1, n + 1):
    numerator = numerator * i

denominator = 1
for j in range(1, k + 1):
    denominator = denominator * j

print(numerator // denominator)
