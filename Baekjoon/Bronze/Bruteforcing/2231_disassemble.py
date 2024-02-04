import sys

input = sys.stdin.readline

n = int(input())


def disassemble(n):
    try:
        for i in range(n - 53, n):
            if i + sum(map(int, str(i))) == n:
                return i
    except:
        for i in range(1, n):
            if i + sum(map(int, str(i))) == n:
                return i
    return 0


print(disassemble(n))
