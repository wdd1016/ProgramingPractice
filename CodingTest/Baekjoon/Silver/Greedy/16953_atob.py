import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def reversedip(start, end, count):
	if start == end:
		return count
	elif start < end:
		return -1
	else:
		if start % 10 == 1:
			return reversedip(start // 10, end, count + 1)
		elif start % 2 == 0:
			return reversedip(start // 2, end, count + 1)
		else:
			return -1

print(reversedip(b, a, 1))