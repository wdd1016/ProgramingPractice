import sys
import heapq
input = sys.stdin.readline

n = int(input())

minHip = []

for _ in range(n):
  x = int(input())
  if x > 0:
    heapq.heappush(minHip, x)
  else:
    if not minHip:
      print(0)
    else:
      print(heapq.heappop(minHip))