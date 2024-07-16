import sys

input = sys.stdin.readline

n = int(input())
countList = [0 for _ in range(n + 1)]
countList[1] = 1


def calculateFourSquares(number):
    partialMinimum = sys.maxsize
    i = 1
    while i * i <= number:
        remain = number - i * i
        partialMinimum = min(partialMinimum, countList[remain])
        i += 1
    countList[number] = partialMinimum + 1


for i in range(2, n + 1):
    calculateFourSquares(i)
print(countList[n])

# DFS로 풀다가 바로 타임아웃
