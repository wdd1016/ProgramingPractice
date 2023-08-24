import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

if n >= 14:
    cnt += n // 14
    n = n % 14

if n >= 7:
    n -= 7
    cnt += 1

cnt += n
    
print(cnt)