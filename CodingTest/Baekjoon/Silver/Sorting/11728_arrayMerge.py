import sys

input = sys.stdin.readline

n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
answer = []

i = 0
j = 0

while i < n and j < m:
    if first[i] <= second[j]:
        answer.append(first[i])
        i += 1

    else:
        answer.append(second[j])
        j += 1

while i < n:
    answer.append(first[i])
    i += 1

while j < m:
    answer.append(second[j])
    j += 1

print(*answer)
