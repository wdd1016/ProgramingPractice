import sys

input = sys.stdin.readline

n = int(input())

answer = [0 for _ in range(n)]
lst = list(map(int, input().split()))

stack = []

for tuple in enumerate(lst):
    while stack and stack[-1][1] < tuple[1]:
        stack.pop()
    if not stack:
        stack.append(tuple)
    else:
        answer[tuple[0]] = stack[-1][0] + 1
        stack.append(tuple)

print(*answer)

# 결국 검색을 통해 monotone stack의 개념을 배우고 적용하여 성공
