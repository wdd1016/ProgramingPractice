import sys
input = sys.stdin.readline

str1 = input().strip()
flag = 'S'
count = 0
for i in range(len(str1)):
	if (str1[i] != ' '):
		if (flag == 'S'):
			count += 1
			flag = 'A'
	else:
		flag = 'S'
print(count)