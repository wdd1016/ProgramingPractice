import sys

input = sys.stdin.readline

n, m = map(int, input().split())

neverHeard = set()

for _ in range(n):
    neverHeard.add(input().rstrip())

answer = []

for _ in range(m):
    name = input().rstrip()
    if name in neverHeard:
        answer.append(name)

answer.sort()
print(len(answer))
print(*answer, sep="\n")
