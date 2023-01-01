import sys
input = sys.stdin.readline

n = int(input())
n -= 1
count = 1
std = 0
while (n > 0):
	std += 6
	n -= std
	count += 1
print(count)
