import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

y_start = 0
minValue = 8 * 8

for y_start in range(n - 7):
    for x_start in range(m - 7):
        count1 = 0
        count2 = 0
        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                if (x + y) % 2 == 0:
                    if board[y][x] == "B":
                        count1 += 1
                    else:
                        count2 += 1
                else:
                    if board[y][x] == "B":
                        count2 += 1
                    else:
                        count1 += 1
        if min(count1, count2) < minValue:
            minValue = min(count1, count2)

print(minValue)
