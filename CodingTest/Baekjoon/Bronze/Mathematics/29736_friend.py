import sys
input = sys.stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())

cnt = 0

for i in range(k-x, k+x+1):
  if i >= a and b >= i:
    cnt += 1

if cnt == 0:
  print("IMPOSSIBLE")
else:
  print(cnt)