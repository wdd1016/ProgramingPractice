import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
lst.sort()

print(*lst)