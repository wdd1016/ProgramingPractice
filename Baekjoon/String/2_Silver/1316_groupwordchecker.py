import sys
input = sys.stdin.readline

def isgroupword(str1):
	lastword = '\0'
	lst = []
	for i in range(len(str1)):
		if (str1[i] == lastword):
			continue
		else:
			if lst.count(str1[i]) > 0:
				return 0
			else:
				lastword = str1[i]
				lst += str1[i]
	return 1

n = int(input())
count = 0
for _ in range(n):
	str1 = input().strip()
	count += isgroupword(str1)
print(count)