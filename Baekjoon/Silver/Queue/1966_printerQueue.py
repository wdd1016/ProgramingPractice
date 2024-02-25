from collections import deque
import sys

input = sys.stdin.readline

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    q = deque(lst)
    lst.sort(reverse=True)

    count = 1
    for target in lst:
        idx = q.index(target)
        if idx > 0:
            q.rotate(-idx)
            m = m - idx
            if m < 0:
                m = m + len(q)
        if m == 0:
            print(count)
            break
        else:
            q.popleft()
            m = m - 1
            count = count + 1
