import sys

input = sys.stdin.readline

MAGIC_NUMBER = 10007

n = int(input())
numberOfCase = [0 for _ in range(1002)]
numberOfCase[1] = 1
numberOfCase[2] = 3

for i in range(3, n + 1):
    numberOfCase[i] = (numberOfCase[i - 2] * 2 + numberOfCase[i - 1]) % MAGIC_NUMBER

print(numberOfCase[n])
