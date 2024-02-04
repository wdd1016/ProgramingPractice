import sys

input = sys.stdin.readline

n = int(input())


def findNum(n):
    number = 666
    count = 0

    while True:
        if "666" in str(number):
            count += 1
            if count == n:
                return number
        number += 1


print(findNum(n))
