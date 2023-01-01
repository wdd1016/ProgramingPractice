import sys
input = sys.stdin.readline

def counttimne(ch):
	stra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(26):
		if (ch == stra[i]):
			if (i < 18):
				time = i // 3 + 3
			elif (i == 18):
				time = 8
			elif (i <= 21):
				time = 9
			else:
				time = 10
			return time

lst = input().strip()
count = 0
for i in range(len(lst)):
	count += counttimne(lst[i])
print(count)