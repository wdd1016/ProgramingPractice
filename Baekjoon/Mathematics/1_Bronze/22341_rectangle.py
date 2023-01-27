import sys
input = sys.stdin.readline

n, c = map(int, input().split())
maxx, maxy = n, n
for i in range(c):
	x, y = map(int, input().split())
	if (x >= maxx or y >= maxy):
		continue
	area1 = maxx * y
	area2 = maxy * x
	if (area1 > area2):
		maxy = y
	else:
		maxx = x
print(maxx * maxy)