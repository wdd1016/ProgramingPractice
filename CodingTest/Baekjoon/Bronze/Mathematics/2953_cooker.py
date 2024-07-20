import sys

input = sys.stdin.readline

winner = 0
max = 0

for i in range(1, 6):
    count = sum(list(map(int, input().split())))
    if count > max:
        winner = i
        max = count

print(winner, max)
