import sys

input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))
cntFruits = [0 for _ in range(10)]

kind = 0
start, end = 0, 0
max = 0

while True:
    if end == n:
        print(end - start)
        break
    elif cntFruits[fruits[end]] == 0:
        kind += 1
    cntFruits[fruits[end]] += 1
    if kind > 2:
        cntFruits[fruits[start]] -= 1
        if cntFruits[fruits[start]] == 0:
            kind -= 1
        start += 1
    end += 1
