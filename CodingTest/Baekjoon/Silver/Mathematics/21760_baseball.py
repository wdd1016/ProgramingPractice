import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
  n, m, k, d = map(int, input().split())

  sameLeagueCoefficient = k * (m - 1) * (n * m) // 2
  otherLeagueCoefficient = (n - 1) * m * (n * m) // 2
  totalLeagueCoefficient = sameLeagueCoefficient + otherLeagueCoefficient
  
  b = d // totalLeagueCoefficient
  if (b > 0):
    print(b * totalLeagueCoefficient)
  else:
    print(-1)