import sys

input = sys.stdin.readline

n = int(input())

minimal = dict()
minimal[1] = 0


def reculsion(num: int) -> int:
    if num in minimal:
        return minimal[num]

    if num % 2 == 0 and num % 3 == 0:
        minimal[num] = min(reculsion(num // 3), reculsion(num // 2)) + 1
    elif num % 3 == 0:
        minimal[num] = min(reculsion(num // 3), reculsion(num - 1)) + 1
    elif num % 2 == 0:
        minimal[num] = min(reculsion(num // 2), reculsion(num - 1)) + 1
    else:
        minimal[num] = reculsion(num - 1) + 1
    return minimal[num]


print(reculsion(n))
