import sys

input = sys.stdin.readline

SIZE = 5

board = [[*map(int, input().split())] for _ in range(5)]
rows, cols, diags = [0 for _ in range(5)], [0 for _ in range(5)], [0 for _ in range(2)]

for i in range(SIZE):
    for j, number in enumerate(map(int, input().split())):
        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] == number:  # board에서 number 찾았을때
                    rows[row] += 1
                    cols[col] += 1
                    if row == col:  # 왼쪽 위에서 오른쪽 아래로 이어지는 대각선
                        diags[0] += 1
                    if row + col == SIZE - 1:  # 오른 위 -> 왼 아래로 이어지는 대각선
                        diags[1] += 1
                    if rows.count(5) + cols.count(5) + diags.count(5) >= 3:
                        print(SIZE * i + j + 1)
                        exit()


# def bingoCheck(field, fieldIdx):
#     global SIZE
#     count = 0
#     for i in range(SIZE):
#         if field[i * SIZE + fieldIdx % 5] != 0:
#             break
#         elif i == SIZE - 1:
#             count += 1
#     for j in range(SIZE):
#         if field[(fieldIdx // 5) * 5 + j] != 0:
#             break
#         elif j == SIZE - 1:
#             count += 1
#     if fieldIdx // 5 == fieldIdx % 5:
#         for i in range(SIZE):
#             if field[i * 5 + i] != 0:
#                 break
#             elif i == SIZE - 1:
#                 count += 1
#     if fieldIdx // 5 == (SIZE - 1 - fieldIdx % 5):
#         for i in range(SIZE):
#             if field[i * 5 + SIZE - 1 - i] != 0:
#                 break
#             elif i == SIZE - 1:
#                 count += 1
#     return count


# field = []
# for _ in range(SIZE):
#     field += map(int, input().split())
# numbers = []
# for _ in range(SIZE):
#     numbers += map(int, input().split())

# bingoCount = 0
# for i, number in enumerate(numbers):
#     fieldIdx = field.index(number)
#     field[fieldIdx] = 0
#     bingoCount += bingoCheck(field, fieldIdx)
#     if bingoCount >= 3:
#         print(i + 1)
#         break
