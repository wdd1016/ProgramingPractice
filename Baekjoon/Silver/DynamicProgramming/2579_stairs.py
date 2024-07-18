import sys

input = sys.stdin.readline

n = int(input())

point = [int(input()) for _ in range(n)]

# score[i] = score[i - 2] + point[i]
# score[i] = score[i - 3] + point[i - 1] + point[i]

score = [0 for _ in range(n)]
score[0] = point[0]
if n >= 2:
    score[1] = point[0] + point[1]
if n >= 3:
    score[2] = max(point[0] + point[2], point[1] + point[2])

for i in range(3, n):
    score[i] = max(score[i - 2] + point[i], score[i - 3] + point[i - 1] + point[i])

print(score[n - 1])
