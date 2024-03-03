import sys

input = sys.stdin.readline

zeroCnt = [0 for _ in range(41)]
oneCnt = [0 for _ in range(41)]

zeroCnt[0] = 1
oneCnt[1] = 1

for i in range(2, 41):
    zeroCnt[i] = zeroCnt[i - 1] + zeroCnt[i - 2]
    oneCnt[i] = oneCnt[i - 1] + oneCnt[i - 2]

t = int(input())

for _ in range(t):
    n = int(input())
    print(zeroCnt[n], oneCnt[n])
