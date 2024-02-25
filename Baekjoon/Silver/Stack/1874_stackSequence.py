import sys

input = sys.stdin.readline

n = int(input())
i = 1

seq = [int(input()) for _ in range(n)]

stack = []
answer = []

for num in seq:
    if stack and stack[-1] == num:
        stack.pop()
        answer.append("-")
        continue
    elif i <= n and i <= num:
        while i <= n and i < num:
            stack.append(i)
            answer.append("+")
            i = i + 1
        if i <= n and i == num:
            answer.append("+")
            answer.append("-")
            i = i + 1
            continue
    answer.append("N")
    break

if answer[-1] == "N":
    print("NO")
else:
    print("\n".join(answer))
