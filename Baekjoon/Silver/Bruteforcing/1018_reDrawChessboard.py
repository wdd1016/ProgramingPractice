import sys, copy

input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(input().rstrip()))

y_start = 0
min = 8 * 8

while y_start <= n - 8:
    x_start = 0
    while x_start <= m - 8:
        count = 0
        board = copy.deepcopy(lst)
        if board[y_start][x_start] == "B":
            count = 1
            board[y_start][x_start] = "W"
        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                if x != x_start and board[y][x] == board[y][x - 1]:
                    count += 1
                    if board[y][x] == "B":
                        board[y][x] = "W"
                    else:
                        board[y][x] = "B"
                elif y != y_start and x == x_start and board[y][x] == board[y - 1][x]:
                    count += 1
                    if board[y][x] == "B":
                        board[y][x] = "W"
                    else:
                        board[y][x] = "B"
        if count < min:
            min = count
        count = 0
        board = copy.deepcopy(lst)
        if board[y_start][x_start] == "W":
            count = 1
            board[y_start][x_start] = "B"
        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                if x != x_start and board[y][x] == board[y][x - 1]:
                    count += 1
                    if board[y][x] == "B":
                        board[y][x] = "W"
                    else:
                        board[y][x] = "B"
                elif y != y_start and x == x_start and board[y][x] == board[y - 1][x]:
                    count += 1
                    if board[y][x] == "B":
                        board[y][x] = "W"
                    else:
                        board[y][x] = "B"
        if count < min:
            min = count
        x_start += 1
    y_start += 1

print(min)
