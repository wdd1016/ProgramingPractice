import sys
input = sys.stdin.readline

n = int(input())
lst = list(set(map(int, input().split())))
lst.sort()
print(*lst)