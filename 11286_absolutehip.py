import sys
import heapq
input = sys.stdin.readline

n = int(input())

negativeHip = []
positiveHip = []

for i in range(n):
  x = int(input())
  if x < 0:
    heapq.heappush(negativeHip, -x)
  elif x > 0:
    heapq.heappush(positiveHip, x)
  else:
    if negativeHip and positiveHip:
      if negativeHip[0] > positiveHip[0]:
        print(heapq.heappop(positiveHip))
      else:
        print(-heapq.heappop(negativeHip))
    elif positiveHip:
      print(heapq.heappop(positiveHip))
    elif negativeHip:
      print(-heapq.heappop(negativeHip))
    else:
      print(0)