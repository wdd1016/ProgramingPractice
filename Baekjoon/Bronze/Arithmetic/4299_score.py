import sys
input = sys.stdin.readline

plus, minus = map(int, input().split())
if (plus < minus):
	print(-1)
elif ((plus + minus) % 2 != 0 or (plus - minus) % 2 != 0):
	print(-1)
else:
	print("%d %d" % ((plus + minus) // 2, (plus - minus) // 2))