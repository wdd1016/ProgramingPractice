import sys
import heapq
input = sys.stdin.readline

n = int(input())

maxHip = []

for _ in range(n):
  x = int(input())
  if x == 0:
    if maxHip:
      print(-heapq.heappop(maxHip))
    else:
      print(0)
  else:
    heapq.heappush(maxHip, -x)