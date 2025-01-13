from collections import deque
import sys

input = sys.stdin.readline


def series(q: deque, n, m):
    if len(q) == m:
        print(*q)
        return
    elif len(q) == 0:
        for i in range(1, n - m + 2):
            q.append(i)
            series(q, n, m)
            q.pop()
    else:
        for i in range(q[-1] + 1, n - m + len(q) + 2):
            q.append(i)
            series(q, n, m)
            q.pop()


n, m = map(int, input().split())
q = deque()
series(q, n, m)
