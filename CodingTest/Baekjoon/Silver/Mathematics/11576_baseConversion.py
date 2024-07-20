import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
nums.reverse()
num = 0

for i in range(m):
    num += nums[i] * (a**i)

result = []

while num:
    result.append(num % b)
    num = num // b

result.reverse()

print(*result)
