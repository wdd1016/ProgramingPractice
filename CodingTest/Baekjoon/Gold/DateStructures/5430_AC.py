import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    funcs = input().rstrip()
    n = int(input())
    if n > 0:
        q = deque(input().rstrip()[1:-1].split(sep=","))
    else:
        q = deque()
        input()

    i = 0
    is_reversed = False
    while i < len(funcs):
        if n == 0 and funcs[i] == "D":
            break
        elif funcs[i] == "D":
            n -= 1
            if is_reversed:
                q.pop()
            else:
                q.popleft()
        else:
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True
        i += 1
    if i < len(funcs):
        print("error")
    elif is_reversed:
        print("[" + ",".join(reversed(list(q))) + "]")
    else:
        print("[" + ",".join(q) + "]")
