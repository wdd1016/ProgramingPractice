from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

minimal = dict()
minimal[n] = 0

queue = deque()
queue.append(n)

while queue:
    num = queue.popleft()
    if num == 1:
        print(minimal[1])
        break
    if num % 3 == 0 and num // 3 not in minimal:
        queue.append(num // 3)
        minimal[num // 3] = minimal[num] + 1
    if num % 2 == 0 and num // 2 not in minimal:
        queue.append(num // 2)
        minimal[num // 2] = minimal[num] + 1
    if num - 1 not in minimal:
        queue.append(num - 1)
        minimal[num - 1] = minimal[num] + 1

# 6의배수에서의 num-1 제외 상황에 대한 해석이 불가능해서 BFS로 전환
# 1에 다가갈수록 count가 증가하는 형식과 큐의 활용으로 최소횟수에 대한 정확한 접근이 가능
