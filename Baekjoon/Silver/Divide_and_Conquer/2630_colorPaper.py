import sys

input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

answer = [0, 0]


def colorCheck(startRow, startCol, size):
    firstColor = paper[startRow][startCol]
    for i in range(startRow, startRow + size):
        for j in range(startCol, startCol + size):
            if paper[i][j] != firstColor:
                return False
    return True


def square(startRow, startCol, size):
    if colorCheck(startRow, startCol, size):
        answer[paper[startRow][startCol]] += 1
        return
    else:
        square(startRow, startCol, size // 2)
        square(startRow + size // 2, startCol, size // 2)
        square(startRow, startCol + size // 2, size // 2)
        square(startRow + size // 2, startCol + size // 2, size // 2)


square(0, 0, n)

print(answer[0])
print(answer[1])
