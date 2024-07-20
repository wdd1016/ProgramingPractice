import sys, math

input = sys.stdin.readline

n = int(input())


def calculateFourSquares(number):
    if math.sqrt(number).is_integer() == True:
        return 1
    for i in range(1, int(math.sqrt(number)) + 1):
        if math.sqrt(number - (i**2)).is_integer() == True:
            return 2
    for i in range(1, int(math.sqrt(number)) + 1):
        for j in range(1, int(math.sqrt(number - (i**2))) + 1):
            if math.sqrt(number - (i**2 + j**2)).is_integer() == True:
                return 3
    return 4


print(calculateFourSquares(n))

# DFS로 풀다가 바로 타임아웃
# DF로 풀다가 타임아웃 (Pypy 성공)
# 4가지 경우라서 해당 내용 도입
