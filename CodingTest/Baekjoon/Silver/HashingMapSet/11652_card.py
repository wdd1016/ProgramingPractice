import sys

input = sys.stdin.readline

cards = dict()

n = int(input())

for _ in range(n):
    i = int(input())
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

answer = 0
maxCount = 0

for number, count in cards.items():
    if count > maxCount:
        answer = number
        maxCount = count
    elif count == maxCount and answer > number:
        answer = number

print(answer)
