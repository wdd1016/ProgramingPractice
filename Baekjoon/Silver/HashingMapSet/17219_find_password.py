import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pwBook = dict()

for _ in range(n):
    key, value = input().rstrip().split()
    pwBook[key] = value

for _ in range(m):
    print(pwBook[input().rstrip()])
