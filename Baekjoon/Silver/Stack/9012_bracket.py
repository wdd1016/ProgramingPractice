import sys

input = sys.stdin.readline

t = int(input())

stack = []

for _ in range(t):
    string = input().rstrip()
    for c in string:
        if c == "(":
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            stack.append(c)
            break
    if stack:
        print("NO")
        stack.clear()
    else:
        print("YES")
