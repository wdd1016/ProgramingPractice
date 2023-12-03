import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
question = list(map(int, input().split()))

counts = [0 for _ in range(20000001)]
for i in lst:
    counts[i] += 1

answer = []
for i in question:
    answer.append(counts[i])

print(*answer)
