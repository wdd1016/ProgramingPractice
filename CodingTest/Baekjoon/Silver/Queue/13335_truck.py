import sys, collections

input = sys.stdin.readline

n, w, L = map(int, input().split())

weight = list(map(int, input().split()))

q = collections.deque([0 for _ in range(w)])

i = 0
currentWeight = 0
time = 0
while q:
    currentWeight -= q.popleft()
    time = time + 1
    if i < n:
        if weight[i] + currentWeight <= L:
            q.append(weight[i])
            currentWeight += weight[i]
            i = i + 1
        else:
            q.append(0)

print(time)
