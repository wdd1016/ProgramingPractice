import sys

input = sys.stdin.readline


def printStar(n):
    if n == 1:
        print("*")
        return
    for i in range(1, n):
        print(" " * (n - i) + "*" * i)
    print("*" * n)
    for i in range(1, n):
        print(" " * i + "*" * (n - i))


n = int(input())

printStar(n)
