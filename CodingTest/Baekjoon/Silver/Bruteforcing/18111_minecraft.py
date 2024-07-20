import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))
ground = Counter(ground)

minTime = 1280000000
correctHeight = 0

for height in range(min(ground.keys()), max(ground.keys()) + 1):
    time = 0
    block = b
    for i, count in ground.items():
        if i == height:
            pass
        elif i > height:
            time += 2 * count * (i - height)
            block += count * (i - height)
        else:
            time += count * (height - i)
            block -= count * (height - i)
    if block >= 0 and time <= minTime:
        minTime = time
        correctHeight = height

print(minTime, correctHeight)
