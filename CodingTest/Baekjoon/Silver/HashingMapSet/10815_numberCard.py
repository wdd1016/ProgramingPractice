import sys

input = sys.stdin.readline

n = int(input())
numCards = set(list(map(int, input().split())))
m = int(input())
findCards = list(map(int, input().split()))
answer = []

for i in range(m):
    if findCards[i] in numCards:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
