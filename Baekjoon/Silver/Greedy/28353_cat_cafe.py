import sys
input = sys.stdin.readline

n , k = map(int, input().split())

weights = list(map(int, input().split()))

weights.sort()

it = 0
rit = n - 1
max = 0

while it < rit:
  if weights[it] + weights[rit] <= k:
    it += 1
    rit -= 1
    max += 1
    continue
  rit -= 1

print(max)