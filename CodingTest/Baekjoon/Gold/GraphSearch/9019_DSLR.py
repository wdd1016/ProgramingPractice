import sys
from collections import deque

input = sys.stdin.readline

# 각 숫자에 대해 가능한 모든 연산 결과를 미리 계산
edge = [
    [(2 * i) % 10000, (i - 1), i // 1000 + (i % 1000) * 10, (i % 10) * 1000 + i // 10]
    for i in range(10000)
]
edge[0][1] = 9999
dir = ["D", "S", "L", "R"]

reverseEdge = [
    # D 연산의 역, 홀수일 때는 적용 불가
    ([i // 2, i // 2 + 5000] if i % 2 == 0 else [])
    + [(i + 1), (i % 10) * 1000 + i // 10, i // 1000 + (i % 1000) * 10]
    for i in range(10000)  # S, L, R 연산의 역
]
reverseEdge[9999][0] = 0
dir_reverse = [("D", "D", "S", "L", "R"), ("S", "L", "R")]


def forward_search(q, edge, dir, visited, visited_reverse, commands, commands_reverse):
    newQ = deque()
    while q:
        num = q.popleft()
        for i in range(len(dir)):  # 정방향 탐색
            newNum = edge[num][i]
            # 서로 다른 방향에서 만났는지 확인 후, 만났다면 경로 출력
            if visited_reverse[newNum] == True:
                print(commands[num] + dir[i] + commands_reverse[newNum])
                return None
            # 방문 여부 확인 후 q에 넣을지 결정
            elif visited[newNum] == False:
                visited[newNum] = True
                commands[newNum] = commands[num] + dir[i]
                newQ.append(newNum)
    return newQ


def backward_search(
    reverseQ,
    reverseEdge,
    dir_reverse,
    visited,
    visited_reverse,
    commands,
    commands_reverse,
):
    newQ = deque()
    while reverseQ:
        num_reverse = reverseQ.popleft()
        dir_now = dir_reverse[num_reverse % 2]
        for i in range(len(dir_now)):  # 역방향 탐색
            newNum_reverse = reverseEdge[num_reverse][i]
            # 서로 다른 방향에서 만났는지 확인 후, 만났다면 경로 출력
            if visited[newNum_reverse] == True:
                print(
                    commands[newNum_reverse]
                    + dir_now[i]
                    + commands_reverse[num_reverse]
                )
                return None
            # 방문 여부 확인 후 q_reverse에 넣을지 결정
            elif visited_reverse[newNum_reverse] == False:
                visited_reverse[newNum_reverse] = True
                commands_reverse[newNum_reverse] = (
                    dir_now[i] + commands_reverse[num_reverse]
                )
                newQ.append(newNum_reverse)
    return newQ


def process(a, b, edge, reverseEdge, dir, dir_reverse):
    visited, visited_reverse = [False] * 10000, [False] * 10000
    commands, commands_reverse = ["" for _ in range(10000)], ["" for _ in range(10000)]

    q, reverseQ = deque([a]), deque([b])
    visited[a] = True
    visited_reverse[b] = True

    while True:
        q = forward_search(
            q, edge, dir, visited, visited_reverse, commands, commands_reverse
        )
        if q is None:
            return
        reverseQ = backward_search(
            reverseQ,
            reverseEdge,
            dir_reverse,
            visited,
            visited_reverse,
            commands,
            commands_reverse,
        )
        if reverseQ is None:
            return


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    process(a, b, edge, reverseEdge, dir, dir_reverse)
