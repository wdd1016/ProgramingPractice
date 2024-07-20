from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
chains = list(map(int, input().split()))
chains.sort()

count = 0
q = deque(chains)
while len(q) > 1:
    min = q.popleft()
    if min < len(q):
        for i in range(min):
            r = q.pop()
            l = q.pop()
            q.append(r + l)
        count += min
    else:
        count += len(q)
        break

print(count)
